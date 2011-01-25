### encoding: utf8 ###
from django.db import models

INFLATION = { 1991: 2.8960067421191402,
              1992: 2.453464625854,
              1993: 2.2432600555178901,
              1994: 2.01645335164558,
              1995: 1.7618257009615901,
              1996: 1.6297568501170301,
              1997: 1.47372841652773,
              1998: 1.3774692123129599,
              1999: 1.2681331112752201,
              2000: 1.25131893632016,
              2001: 1.25131893632016,
              2002: 1.2339281885664299,
              2003: 1.15866084989269,
              2004: 1.1809348973841101,
              2005: 1.1668481988066199,
              2006: 1.1396595029126499,
              2007: 1.1407670437322399,
              2008: 1.1032936585367299,
              2009: 1.06285338345858,
              2010: 1.02281368821293,
              2011: 1.0,
              2012: 1.0, }


class BudgetLine(models.Model):
    
    title               = models.CharField( max_length=256, db_index=True )
    budget_id           = models.CharField( max_length=64,db_index=True )
    budget_id_len       = models.PositiveIntegerField( default=0, db_index=True )
    
    net_amount_allocated    = models.IntegerField( null = True )
    net_amount_revised        = models.IntegerField( null = True )
    net_amount_used         = models.IntegerField( null = True ) 
    gross_amount_allocated    = models.IntegerField( null = True )
    gross_amount_revised        = models.IntegerField( null = True )
    gross_amount_used         = models.IntegerField( null = True ) 
    
    year                = models.PositiveIntegerField( db_index=True )
    
    containing_line     = models.ForeignKey( 'self', related_name='sublines', null=True, db_index=True )

    @property
    def inflation_factor(self): return INFLATION.get(self.year, 1)

    def _amount_allocated(self):
        return "<label title='סכום לפני התחשבות במדד: %s'>%s</label>" % ( self.amount_allocated, int(self.inflation_factor*self.amount_allocated) ) 
    _amount_allocated.short_description = u'הקצאה (באלפי \u20aa)'
    _amount_allocated.allow_tags = True

    def _amount_revised(self):
        return "<label title='סכום לפני התחשבות במדד: %s'>%s</label>" % ( self.amount_revised, int(self.inflation_factor*self.amount_revised) ) 
    _amount_revised.short_description = u'הקצאה מעודכנת (באלפי \u20aa)'
    _amount_revised.allow_tags = True

    def _amount_used(self):
        return "<label title='סכום לפני התחשבות במדד: %s'>%s</label>" % ( self.amount_used, int(self.inflation_factor*self.amount_used) ) 
    _amount_used.short_description = u'ניצול (באלפי \u20aa)'
    _amount_used.allow_tags = True
    
    def _title(self):
        return "<a href='/admin/budget_lines/budgetline/my/?q=%s&year=%s&ot=asc&o=1'>%s</a>" % (self.budget_id, self.year, self.title )
    _title.short_description = u'שם'
    _title.allow_tags = True
    
    def parent_budget_id(self):
        if self.containing_line == None:
            return u'אין'
        else:
            return "<a href='/admin/budget_lines/budgetline/my/?q=%s&year=%s&ot=asc&o=1'>%s</a>" % (self.containing_line.budget_id, self.containing_line.year, self.containing_line.title)
    parent_budget_id.short_description = u'סעיף אב'
    parent_budget_id.allow_tags = True
