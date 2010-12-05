# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding index on 'BudgetLine', fields ['title']
        db.create_index('obudget_budgetline', ['title'])

        # Adding index on 'BudgetLine', fields ['budget_id']
        db.create_index('obudget_budgetline', ['budget_id'])

        # Adding index on 'BudgetLine', fields ['year']
        db.create_index('obudget_budgetline', ['year'])


    def backwards(self, orm):
        
        # Removing index on 'BudgetLine', fields ['title']
        db.delete_index('obudget_budgetline', ['title'])

        # Removing index on 'BudgetLine', fields ['budget_id']
        db.delete_index('obudget_budgetline', ['budget_id'])

        # Removing index on 'BudgetLine', fields ['year']
        db.delete_index('obudget_budgetline', ['year'])


    models = {
        'obudget.budgetline': {
            'Meta': {'object_name': 'BudgetLine'},
            'amount_allocated': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'amount_used': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'budget_id': ('django.db.models.fields.CharField', [], {'max_length': '64', 'db_index': 'True'}),
            'containing_line': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sublines'", 'null': 'True', 'to': "orm['obudget.BudgetLine']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.TextField', [], {'db_index': 'True'}),
            'year': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        }
    }

    complete_apps = ['obudget']
