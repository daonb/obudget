import sys
import cPickle
import re
from obudget.budget_lines.models import BudgetLine 
from django.core.management.base import BaseCommand

class Command(BaseCommand):

    args = '<pickle-file>'
    help = 'Parses pickle''d budget data into the DB'

    def handle(self, *args, **options):
        multi_ws = re.compile('[\r\n\t ]+')
        
        BudgetLine.objects.all().delete()
        
        b = cPickle.load(file(args[0]))
        
        for year,lines in b.iteritems():
            for line in lines:
                allocated = line['budget1']
                allocated = 0 if allocated == None else int(allocated)
                revised = line['budget2']
                revised = allocated if revised == None else int(revised)
                used = line['implementation']
                used = 0 if used == None else int(used)
                if used < 0 or allocated < 0:
                    continue
                title = line['description']
                title = multi_ws.sub(title,' ')   
                budget_id = line['num']
                
                BudgetLine( title = title,
                            budget_id = budget_id,
                            amount_allocated = allocated,
                            amount_revised = revised,
                            amount_used = used,
                            year = year,
                            ).save()
            
        