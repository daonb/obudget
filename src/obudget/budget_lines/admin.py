from django.contrib import admin
from obudget.budget_lines.models import BudgetLine 

class BudgetLineAdmin(admin.ModelAdmin):
    fields =  ( 'budget_id', 'title', 'year', 'amount_allocated', 'amount_revised', 'amount_used' )
    readonly_fields =  ( 'budget_id', 'title', 'year', 'amount_allocated', 'amount_revised', 'amount_used' )
    list_display =  ( 'budget_id', '_title', 'year', '_amount_allocated', '_amount_revised', '_amount_used', 'parent_budget_id' )
    list_filter = ( 'year', )
    ordering = ( '-year', 'budget_id',)
    search_fields = ( '^budget_id', 'title', )
    actions_on_top = False
    actions_on_bottom = False
    
admin.site.register(BudgetLine, BudgetLineAdmin)

