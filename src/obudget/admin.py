from django.contrib import admin
from obudget import models 

class BudgetLineAdmin(admin.ModelAdmin):
    fields =  ( 'budget_id', 'title', 'year', 'amount_allocated', 'amount_used' )
    list_display =  ( 'budget_id', 'title', 'year', 'amount_allocated', 'amount_used' )
    list_filter = ( 'year', )
    search_fields = ( 'budget_id', 'title', )
    
admin.site.register(models.BudgetLine, BudgetLineAdmin)
