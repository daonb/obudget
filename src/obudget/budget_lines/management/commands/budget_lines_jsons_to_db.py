import sys
import csv
import re
from obudget.budget_lines.models import BudgetLine 
from django.core.management.base import BaseCommand
import json

class Command(BaseCommand):

    args = '<jsons-file> <jsons-file> ...'
    help = 'Transfers jsons budget data files into the DB'

    def handle(self, *args, **options):

        print 'Loading raw rows'
        k = 0
        for filename in args:
            print filename
            for l in file(filename).readlines():
                d = json.loads(l)
                bl, _ = BudgetLine.objects.get_or_create( budget_id = d['code'], year = d['year'] )
                bl.title = d.get('title',bl.title)
                bl.net_amount_allocated = d.get('net_allocated',bl.net_amount_allocated)
                bl.net_amount_revised = d.get('net_revised',bl.net_amount_revised)
                bl.net_amount_used = d.get('net_used',bl.net_amount_used)
                bl.gross_amount_allocated = d.get('gross_allocated',bl.gross_amount_allocated)
                bl.gross_amount_revised = d.get('gross_revised',bl.gross_amount_revised)
                bl.gross_amount_used = d.get('gross_used',bl.gross_amount_used)

                bl.budget_id_len = len(bl.budget_id)
                bl.save()

                k+=1
                if k % 1000 == 0:
                    print k
        
        # Update internal relationships in the DB
        print 'Internal relationships'
        for line in BudgetLine.objects.filter( containing_line__isnull = True, budget_id_len__gt=2 ):
            k+=1
            if k % 1000 == 0:
                print k

            if line.budget_id == None or len(line.budget_id) == 2:        
                continue
            
            for i in range(2,len(line.budget_id),2):
                parent_budget_id  = line.budget_id[:-i]
                parents = BudgetLine.objects.filter( year = line.year, budget_id = parent_budget_id, budget_id_len = len(parent_budget_id) ).count()
                if parents > 0:
                    parent = BudgetLine.objects.get( year = line.year, budget_id = parent_budget_id, budget_id_len = len(parent_budget_id) )
                    line.containing_line = parent
                    line.save()
                    break
        