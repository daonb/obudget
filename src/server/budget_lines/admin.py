from django.contrib import admin
from django.contrib.auth.models import User, Permission
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from django.conf.urls.defaults import patterns, url
from models import BudgetLine 

class BudgetLineAdmin(admin.ModelAdmin):
    fields =  ( 'budget_id', 'title', 'year', 'amount_allocated', 'amount_revised', 'amount_used' )
    readonly_fields =  ( 'budget_id', 'title', 'year', 'amount_allocated', 'amount_revised', 'amount_used' )
    list_display =  ( 'budget_id', '_title', 'year', '_amount_allocated', '_amount_revised', '_amount_used', 'parent_budget_id' )
    list_filter = ( 'year', )
    ordering = ( '-year', 'budget_id',)
    search_fields = ( '^budget_id', 'title', )
    actions_on_top = False
    actions_on_bottom = False

    def autologin(self,request,upper,*args,**kw):
        if not request.user.is_authenticated():
            default_user, _ = User.objects.get_or_create( username='budget' )
            default_user.set_password('supersecretbudgetpassword')
            default_user.is_staff=True
            perm = Permission.objects.get(codename='change_budgetline')
            default_user.user_permissions.add(perm)
            default_user.save()
            user = authenticate(username='budget', password='supersecretbudgetpassword')
            login(request, user)
            return HttpResponseRedirect(request.get_full_path())

        return upper(request,*args,**kw)

    def my_changelist_view(self, request, *args, **kw):
        return self.autologin(request,super(BudgetLineAdmin,self).changelist_view,*args,**kw)

    def my_change_view(self, request, *args, **kw):
        return self.autologin(request,super(BudgetLineAdmin,self).change_view,*args,**kw)

    def get_urls(self):
        info = self.model._meta.app_label, self.model._meta.module_name
        urlpatterns = patterns('',
            url(r'^my/$',
                self.my_changelist_view,
                name='%s_%s_mychangelist' % info ),
            url(r'^my/(.+)/$',
                self.my_change_view,
                name='%s_%s_mychange' % info),
 
            )
        urlpatterns += super(BudgetLineAdmin,self).get_urls()
        return urlpatterns
        

admin.site.register(BudgetLine, BudgetLineAdmin)

