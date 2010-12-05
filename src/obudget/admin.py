from django.contrib import admin
from budget_lines.models import BudgetLine 

class BudgetLineAdmin(admin.ModelAdmin):
    fields =  ( 'budget_id', 'title', 'year', 'amount_allocated', 'amount_used' )
    list_display =  ( 'budget_id', 'title', 'year', 'amount_allocated', 'amount_used' )
    list_filter = ( 'year', )
    search_fields = ( 'budget_id', 'title', )
    
admin.site.register(BudgetLine, BudgetLineAdmin)
