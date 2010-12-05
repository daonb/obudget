from datetime import datetime
import urllib
from django.db.models import Q
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.core.cache import cache
from django.db.models import Count
from piston.resource import Resource
from piston.handler import BaseHandler
from piston.utils import rc
from obudget.budget_lines.models import BudgetLine

DEFAULT_PAGE_LEN = 20
def limit_by_request(qs, request):
    if 'num' in request.GET:
        num = int(request.GET['num'])
        page = 'page' in request.GET and int(request.GET['page']) or 0
        return qs[page*num:(page+1)*num]
    return qs

class BudgetLineHandler(BaseHandler):
    allowed_methods = ('GET')
    model = BudgetLine
    qs = BudgetLine.objects.all()
    fields = ('title', 'budget_id', 'amount_allocated',
	      'amount_revised', 'amount_used', 'year')
    def read(self, request, **kwargs):
	r = self.qs.filter(budget_id__startswith=kwargs["id"])
	return self.qs.filter(budget_id__startswith=kwargs["id"])
        return super(BudgetLineHandler, self).read(request, **kwargs)

budget_line_handler= Resource(BudgetLineHandler)

