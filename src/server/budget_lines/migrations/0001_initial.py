# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'BudgetLine'
        db.create_table('budget_lines_budgetline', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(db_index=True,max_length=256)),
            ('budget_id', self.gf('django.db.models.fields.CharField')(max_length=64, db_index=True)),
            ('amount_allocated', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('amount_used', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('year', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('containing_line', self.gf('django.db.models.fields.related.ForeignKey')(related_name='sublines', null=True, to=orm['budget_lines.BudgetLine'])),
        ))
        db.send_create_signal('budget_lines', ['BudgetLine'])


    def backwards(self, orm):
        
        # Deleting model 'BudgetLine'
        db.delete_table('budget_lines_budgetline')


    models = {
        'budget_lines.budgetline': {
            'Meta': {'object_name': 'BudgetLine'},
            'amount_allocated': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'amount_used': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'budget_id': ('django.db.models.fields.CharField', [], {'max_length': '64', 'db_index': 'True'}),
            'containing_line': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sublines'", 'null': 'True', 'to': "orm['budget_lines.BudgetLine']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'db_index': 'True','max_length':'256'}),
            'year': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        }
    }

    complete_apps = ['budget_lines']
