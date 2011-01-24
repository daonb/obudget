# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'BudgetLine.amount_allocated'
        db.delete_column('budget_lines_budgetline', 'amount_allocated')

        # Deleting field 'BudgetLine.amount_used'
        db.delete_column('budget_lines_budgetline', 'amount_used')

        # Deleting field 'BudgetLine.amount_revised'
        db.delete_column('budget_lines_budgetline', 'amount_revised')

        # Adding field 'BudgetLine.net_amount_allocated'
        db.add_column('budget_lines_budgetline', 'net_amount_allocated', self.gf('django.db.models.fields.PositiveIntegerField')(null=True), keep_default=False)

        # Adding field 'BudgetLine.net_amount_revised'
        db.add_column('budget_lines_budgetline', 'net_amount_revised', self.gf('django.db.models.fields.PositiveIntegerField')(null=True), keep_default=False)

        # Adding field 'BudgetLine.net_amount_used'
        db.add_column('budget_lines_budgetline', 'net_amount_used', self.gf('django.db.models.fields.PositiveIntegerField')(null=True), keep_default=False)

        # Adding field 'BudgetLine.gross_amount_allocated'
        db.add_column('budget_lines_budgetline', 'gross_amount_allocated', self.gf('django.db.models.fields.PositiveIntegerField')(null=True), keep_default=False)

        # Adding field 'BudgetLine.gross_amount_revised'
        db.add_column('budget_lines_budgetline', 'gross_amount_revised', self.gf('django.db.models.fields.PositiveIntegerField')(null=True), keep_default=False)

        # Adding field 'BudgetLine.gross_amount_used'
        db.add_column('budget_lines_budgetline', 'gross_amount_used', self.gf('django.db.models.fields.PositiveIntegerField')(null=True), keep_default=False)

        # Adding index on 'BudgetLine', fields ['budget_id_len']
        db.create_index('budget_lines_budgetline', ['budget_id_len'])


    def backwards(self, orm):
        
        # Adding field 'BudgetLine.amount_allocated'
        db.add_column('budget_lines_budgetline', 'amount_allocated', self.gf('django.db.models.fields.PositiveIntegerField')(default=0), keep_default=False)

        # Adding field 'BudgetLine.amount_used'
        db.add_column('budget_lines_budgetline', 'amount_used', self.gf('django.db.models.fields.PositiveIntegerField')(default=0), keep_default=False)

        # Adding field 'BudgetLine.amount_revised'
        db.add_column('budget_lines_budgetline', 'amount_revised', self.gf('django.db.models.fields.PositiveIntegerField')(null=True), keep_default=False)

        # Deleting field 'BudgetLine.net_amount_allocated'
        db.delete_column('budget_lines_budgetline', 'net_amount_allocated')

        # Deleting field 'BudgetLine.net_amount_revised'
        db.delete_column('budget_lines_budgetline', 'net_amount_revised')

        # Deleting field 'BudgetLine.net_amount_used'
        db.delete_column('budget_lines_budgetline', 'net_amount_used')

        # Deleting field 'BudgetLine.gross_amount_allocated'
        db.delete_column('budget_lines_budgetline', 'gross_amount_allocated')

        # Deleting field 'BudgetLine.gross_amount_revised'
        db.delete_column('budget_lines_budgetline', 'gross_amount_revised')

        # Deleting field 'BudgetLine.gross_amount_used'
        db.delete_column('budget_lines_budgetline', 'gross_amount_used')

        # Removing index on 'BudgetLine', fields ['budget_id_len']
        db.delete_index('budget_lines_budgetline', ['budget_id_len'])


    models = {
        'budget_lines.budgetline': {
            'Meta': {'object_name': 'BudgetLine'},
            'budget_id': ('django.db.models.fields.CharField', [], {'max_length': '64', 'db_index': 'True'}),
            'budget_id_len': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'db_index': 'True'}),
            'containing_line': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sublines'", 'null': 'True', 'to': "orm['budget_lines.BudgetLine']"}),
            'gross_amount_allocated': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'gross_amount_revised': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'gross_amount_used': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'net_amount_allocated': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'net_amount_revised': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'net_amount_used': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'title': ('django.db.models.fields.TextField', [], {'db_index': 'True'}),
            'year': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        }
    }

    complete_apps = ['budget_lines']
