import sys
import csv
import re
from obudget.budget_lines.models import BudgetLine 
from django.core.management.base import BaseCommand

class Command(BaseCommand):

    args = '<csv-file>'
    help = 'Parses csv''d budget data into the DB'

    def handle(self, *args, **options):

        reader = csv.DictReader(file(args[0]), ['year','title','budget_id','allocated','revised','used'])
       
        print 'Deleting current rows'
        BudgetLine.objects.all().delete()
                
        print 'Loading raw rows'
        i = 0
        for d in reader:              
            BudgetLine( title = d['title'].decode('utf8'),
                        budget_id = d['budget_id'],
                        amount_allocated = int(d['allocated']),
                        amount_revised = int(d['revised']),
                        amount_used = int(d['used']),
                        year = int(d['year']),
                        ).save()
            i+=1
            if i % 1000 == 0:
                print i

        
        # Update internal relationships in the DB
        print 'Internal relationships'
        i = 0
        for line in BudgetLine.objects.all():
            i+=1
            if i % 1000 == 0:
                print i

            if line.budget_id == None or len(line.budget_id) == 2:        
                continue
            
            for i in range(2,len(line.budget_id),2):
                try:
                    parent = BudgetLine.objects.get( year = line.year, budget_id = line.budget_id[:-i] )
                    line.containing_line = parent
                    line.save()
                    break
                except:
                    pass
            
        
        