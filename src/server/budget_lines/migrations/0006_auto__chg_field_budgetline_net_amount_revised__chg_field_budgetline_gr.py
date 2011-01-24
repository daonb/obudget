# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'BudgetLine.net_amount_revised'
        db.alter_column('budget_lines_budgetline', 'net_amount_revised', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'BudgetLine.gross_amount_used'
        db.alter_column('budget_lines_budgetline', 'gross_amount_used', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'BudgetLine.gross_amount_revised'
        db.alter_column('budget_lines_budgetline', 'gross_amount_revised', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'BudgetLine.net_amount_allocated'
        db.alter_column('budget_lines_budgetline', 'net_amount_allocated', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'BudgetLine.net_amount_used'
        db.alter_column('budget_lines_budgetline', 'net_amount_used', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'BudgetLine.gross_amount_allocated'
        db.alter_column('budget_lines_budgetline', 'gross_amount_allocated', self.gf('django.db.models.fields.IntegerField')(null=True))


    def backwards(self, orm):
        
        # Changing field 'BudgetLine.net_amount_revised'
        db.alter_column('budget_lines_budgetline', 'net_amount_revised', self.gf('django.db.models.fields.PositiveIntegerField')(null=True))

        # Changing field 'BudgetLine.gross_amount_used'
        db.alter_column('budget_lines_budgetline', 'gross_amount_used', self.gf('django.db.models.fields.PositiveIntegerField')(null=True))

        # Changing field 'BudgetLine.gross_amount_revised'
        db.alter_column('budget_lines_budgetline', 'gross_amount_revised', self.gf('django.db.models.fields.PositiveIntegerField')(null=True))

        # Changing field 'BudgetLine.net_amount_allocated'
        db.alter_column('budget_lines_budgetline', 'net_amount_allocated', self.gf('django.db.models.fields.PositiveIntegerField')(null=True))

        # Changing field 'BudgetLine.net_amount_used'
        db.alter_column('budget_lines_budgetline', 'net_amount_used', self.gf('django.db.models.fields.PositiveIntegerField')(null=True))

        # Changing field 'BudgetLine.gross_amount_allocated'
        db.alter_column('budget_lines_budgetline', 'gross_amount_allocated', self.gf('django.db.models.fields.PositiveIntegerField')(null=True))


    models = {
        'budget_lines.budgetline': {
            'Meta': {'object_name': 'BudgetLine'},
            'budget_id': ('django.db.models.fields.CharField', [], {'max_length': '64', 'db_index': 'True'}),
            'budget_id_len': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'db_index': 'True'}),
            'containing_line': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sublines'", 'null': 'True', 'to': "orm['budget_lines.BudgetLine']"}),
            'gross_amount_allocated': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'gross_amount_revised': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'gross_amount_used': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'net_amount_allocated': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'net_amount_revised': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'net_amount_used': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256', 'db_index': 'True'}),
            'year': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        }
    }

    complete_apps = ['budget_lines']
