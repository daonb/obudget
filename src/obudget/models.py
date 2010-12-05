from django.db import models

class BudgetLine(models.Model):
    
    title               = models.TextField(db_index=True)
    budget_id           = models.CharField(max_length=64,db_index=True)
    
    amount_allocated    = models.PositiveIntegerField()
    amount_used         = models.PositiveIntegerField() 
    
    year                = models.PositiveIntegerField(db_index=True)
    
    containing_line     = models.ForeignKey('self',related_name='sublines',null=True,db_index=True)
    
    