from django.contrib import admin
from obudget.budget_lines.models import BudgetLine 

class BudgetLineAdmin(admin.ModelAdmin):
    fields =  ( 'budget_id', 'title', 'year', 'amount_allocated', 'amount_revised', 'amount_used' )
    readonly_fields =  ( 'budget_id', 'title', 'year', 'amount_allocated', 'amount_revised', 'amount_used' )
    list_display =  ( 'budget_id', 'title', 'year', 'amount_allocated', 'amount_revised', 'amount_used' )
    list_filter = ( 'year', )
    ordering = ( '-year', 'budget_id',)
    search_fields = ( 'budget_id', 'title', )
    actions_on_top = False
    actions_on_bottom = False
    
admin.site.register(BudgetLine, BudgetLineAdmin)
