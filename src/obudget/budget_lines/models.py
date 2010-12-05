### encoding: utf8 ###

from django.db import models

class BudgetLine(models.Model):

    class Meta:
        verbose_name = u'שורת תקציב'
        verbose_name_plural = u'שורות תקציב'
    
    title               = models.TextField( db_index=True,
                                            verbose_name=u'שם' )
    budget_id           = models.CharField( max_length=64,db_index=True,
                                            verbose_name=u'סעיף' )
    
    amount_allocated    = models.PositiveIntegerField( verbose_name=u'הקצאה (באלפי \u20aa)' )
    amount_revised    	= models.PositiveIntegerField( null=True,
                                                       verbose_name=u'הקצאה מעודכנת (באלפי \u20aa)' )
    amount_used         = models.PositiveIntegerField( verbose_name=u'ניצול (באלפי \u20aa)' ) 
    
    year                = models.PositiveIntegerField( db_index=True,
                                                       verbose_name=u'שנה' )
    
    containing_line     = models.ForeignKey( 'self', related_name='sublines', null=True, db_index=True,
                                              verbose_name=u'סעיף אב' )
