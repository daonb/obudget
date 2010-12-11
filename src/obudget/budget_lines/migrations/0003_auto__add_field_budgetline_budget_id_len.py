# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'BudgetLine.budget_id_len'
        db.add_column('budget_lines_budgetline', 'budget_id_len', self.gf('django.db.models.fields.PositiveIntegerField')(default=0), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'BudgetLine.budget_id_len'
        db.delete_column('budget_lines_budgetline', 'budget_id_len')


    models = {
        'budget_lines.budgetline': {
            'Meta': {'object_name': 'BudgetLine'},
            'amount_allocated': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'amount_revised': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'amount_used': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'budget_id': ('django.db.models.fields.CharField', [], {'max_length': '64', 'db_index': 'True'}),
            'budget_id_len': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'containing_line': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sublines'", 'null': 'True', 'to': "orm['budget_lines.BudgetLine']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.TextField', [], {'db_index': 'True'}),
            'year': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        }
    }

    complete_apps = ['budget_lines']
