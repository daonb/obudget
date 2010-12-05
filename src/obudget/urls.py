from django.conf.urls.defaults import *

from obudget import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.contrib.auth.models import User, Permission
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^obudget/', include('obudget.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^$', views.main),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)


default_user, created = User.objects.get_or_create( username='budget' )
default_user.set_password('budget')
default_user.is_staff=True
perm = Permission.objects.get(codename='change_budgetline')
default_user.user_permissions.add(perm)
default_user.save()
    