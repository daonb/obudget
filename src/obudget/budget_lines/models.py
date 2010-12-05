### encoding: utf8 ###
from django.db import models

INFLATION = { 1992: 2.4346008563961177,
              1993: 2.1746274377250385,
              1994: 1.9599492230962552,
              1995: 1.7452798068532993,
              1996: 1.5857194361620188,
              1997: 1.4243817028315808,
              1998: 1.3066328153975035,
              1999: 1.2396895781759996,
              2000: 1.1784121465551327,
              2001: 1.1651217839999997,
              2002: 1.1524448902077149,
              2003: 1.0909379999999997,
              2004: 1.0833545183714,
              2005: 1.0876749750747754,
              2006: 1.0737578740157478,
              2007: 1.0509999999999999,
              2008: 1.0457711442786071,
              2009: 1 }

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

    @property
    def inf_amount_allocated(self):
        infl = INFLATION[self.year]
        return int(infl*self.amount_allocated)
    
    def _amount_allocated(self):
        return "<label title='סכום לפני התחשבות במדד: %s'>%s</label>" % ( self.amount_allocated, self.inf_amount_allocated ) 
    _amount_allocated.short_description = u'הקצאה (באלפי \u20aa)'
    _amount_allocated.allow_tags = True

    @property
    def inf_amount_revised(self):
        infl = INFLATION[self.year]
        return int(infl*self.amount_revised)

    def _amount_revised(self):
        return "<label title='סכום לפני התחשבות במדד: %s'>%s</label>" % ( self.amount_revised, self.inf_amount_revised ) 
    _amount_revised.short_description = u'הקצאה מעודכנת (באלפי \u20aa)'
    _amount_revised.allow_tags = True

    @property
    def inf_amount_used(self):
        infl = INFLATION[self.year]
        return int(infl*self.amount_used)

    def _amount_used(self):
        return "<label title='סכום לפני התחשבות במדד: %s'>%s</label>" % ( self.amount_used, self.inf_amount_used) 
    _amount_used.short_description = u'ניצול (באלפי \u20aa)'
    _amount_used.allow_tags = True
    
    def _title(self):
        return "<a href='/admin/budget_lines/budgetline/my/?q=%s&year=%s&ot=asc&o=1'>%s</a>" % (self.budget_id, self.year, self.title)
    _title.short_description = u'שם'
    _title.allow_tags = True
    
    def parent_budget_id(self):
        if self.containing_line == None:
            return u'אין'
        else:
            return "<a href='/admin/budget_lines/budgetline/my/?q=%s&year=%s&ot=asc&o=1'>%s</a>" % (self.containing_line.budget_id, self.containing_line.year, self.containing_line.title)
    parent_budget_id.short_description = u'סעיף אב'
    parent_budget_id.allow_tags = True