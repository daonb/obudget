import sys
import cPickle
import re
import csv
from obudget.budget_lines.models import BudgetLine 
from django.core.management.base import BaseCommand

class Command(BaseCommand):

    args = '<csv-file>'
    help = 'Parses csv''d budget data into the db'

    def handle(self, *args, **options):
        
        writer = csv.DictWriter(file(args[1],'w'), ['year','title','budget_id','allocated','revised','used'])
        
        multi_ws = re.compile(u'\s+')
        
        b = cPickle.load(file(args[0]))
        
        for year,lines in b.iteritems():
            for line in lines:
                allocated = line['budget1']
                allocated = 0 if allocated == None else int(allocated)
                revised = line['budget2']
                revised = allocated if revised == None else int(revised)
                used = line['implementation']
                used = 0 if used == None else int(used)
                title = line['description']
                title = multi_ws.sub(' ',title,re.U)   
                budget_id = line['num']
                
                d = { 'year'      : year,
                      'title'     : title.encode('utf8'),
                      'budget_id' : budget_id,
                      'allocated' : allocated,
                      'revised'   : revised,
                      'used'      : used,
                      }                
                print title
                writer.writerow(d) 
                        