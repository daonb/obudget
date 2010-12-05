"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase
from django.core.urlresolvers import reverse
from models import *

class APITest(TestCase):
    def setUp(self):
    	self.line1 = BudgetLine.objects.create(title="line 1", budget_id="0001",
		amount_allocated=2, amount_revised=20, amount_used=18, year=1970)
    	self.line11 = BudgetLine.objects.create(title="line 101", budget_id="000101",
		amount_allocated=12, amount_revised=15, amount_used=13, year=1970)

    def test_basic_line(self):
	import json

	res = self.client.get(reverse('budget-line-handler', kwargs={'id':'000101'}))
        self.assertEqual(res.status_code, 200)
	data = json.loads(res.content, encoding='utf8')
	self.assertEqual(data, [{u'title': u'line 101', u'amount_allocated': 12, u'budget_id': u'000101', u'year': 1970, u'amount_revised': 15, u'amount_used': 13}])
	res = self.client.get(reverse('budget-line-handler', kwargs={'id':'0001'}))
        self.assertEqual(res.status_code, 200)
	data = json.loads(res.content, encoding='utf8')
	self.assertEqual(len(data), 2)
	# TODO: test content
