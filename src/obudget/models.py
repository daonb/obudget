from django.db import models
from django.db.models.fields.related import RECURSIVE_RELATIONSHIP_CONSTANT

class BudgetLine(models.Model):
    
    title               = models.TextField()
    budget_id           = models.CharField(max_length=64)
    
    amount_allocated    = models.PositiveIntegerField()
    amount_used         = models.PositiveIntegerField() 
    
    year                = models.PositiveIntegerField()
    
    containing_line     = models.ForeignKey('self',related_name='sublines',null=True)
    
    