import sys
import cPickle
import re
from obudget.budget_lines.models import BudgetLine 
from django.core.management.base import BaseCommand

class Command(BaseCommand):

    args = ''
    help = 'Update internal relationships in the DB'

    def handle(self, *args, **options):

        for line in BudgetLine.objects.all():
            if line.budget_id == None or len(line.budget_id) == 2:
                
                continue
            try:
                parent = BudgetLine.objects.get( year = line.year, budget_id = line.budget_id[:-2] )
                line.containing_line = parent
                line.save()
                print '%s >> %s' % (parent.title, line.title )
            except:
                continue
            
        