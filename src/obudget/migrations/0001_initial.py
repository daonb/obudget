# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'BudgetLine'
        db.create_table('obudget_budgetline', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.TextField')()),
            ('budget_id', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('amount_allocated', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('amount_used', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('year', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('containing_line', self.gf('django.db.models.fields.related.ForeignKey')(related_name='sublines', null=True, to=orm['obudget.BudgetLine'])),
        ))
        db.send_create_signal('obudget', ['BudgetLine'])


    def backwards(self, orm):
        
        # Deleting model 'BudgetLine'
        db.delete_table('obudget_budgetline')


    models = {
        'obudget.budgetline': {
            'Meta': {'object_name': 'BudgetLine'},
            'amount_allocated': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'amount_used': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'budget_id': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'containing_line': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sublines'", 'null': 'True', 'to': "orm['obudget.BudgetLine']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.TextField', [], {}),
            'year': ('django.db.models.fields.PositiveIntegerField', [], {})
        }
    }

    complete_apps = ['obudget']
