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
from django.db.models.expressions import F
from django.db.models.aggregates import Max


DEFAULT_PAGE_LEN = 20
def limit_by_request(qs, request):
    if 'num' in request.GET or 'page' in request.GET:
        num = int(request.GET.get('num',DEFAULT_PAGE_LEN))
        page = int(request.GET.get('page',0))
        return qs[page*num:(page+1)*num]
    return qs

def year_by_request(qs, request):
    if 'year' in request.GET:
        year = int(request.GET['year'])
        return qs.filter(year=year)
    return qs

def text_by_request(qs, request):
    if 'text' in request.GET:
        text = request.GET['text']
        return qs.filter(title__icontains = text)
    return qs

def distinct_by_request(qs, request):
    if 'distinct' in request.GET and request.GET['distinct']=="1":
#        return qs.order_by('budget_id_len','budget_id').values('title','budget_id','containing_line').distinct()
        qs = qs.order_by('budget_id_len','budget_id')
        qs.query.group_by = ['budget_id']

    
        #       annotate(max_year=Max('year')).filter(year=F('max_year')).order_by('budget_id_len','budget_id')
    else:
        return qs.order_by('-year','budget_id_len','budget_id')
    return qs

def depth_by_request(qs, request, budget_code):
    start_depth = len(budget_code)
    depth = request.GET.get('depth',0)
    full = request.GET.get('full',None) == '1'
    if full:
        depth = 20 # to be on the safe side
    if depth != None:
        max_depth = start_depth + int(depth)*2
        qs = qs.filter( budget_id_len__lte = max_depth ) 
    return qs

class BudgetLineHandler(BaseHandler):
    '''
    API Documentation:
    ------------------
    
    <url>/<budget-code>/?<params>
    
    params:
    ------
    year  - year selection
    num   - page size
    page  - page index
    full  - 1/0, bring full subtree(s)
    depth - >0, bring x layers of subtree(s)
    text  - search term, bring entries which contain the text
    distinct - return distinct records (same title, code, parents), and no year information 
    '''

    allowed_methods = ('GET')
    model = BudgetLine
    qs = BudgetLine.objects.all()
    fields = ('title', 'budget_id', 
              'net_amount_allocated','net_amount_revised', 'net_amount_used', 
              'gross_amount_allocated','gross_amount_revised', 'gross_amount_used', 
              'inflation_factor', 
              'year',
              'parent',
              )
    
    def read(self, request, **kwargs):
        budget_code = kwargs["id"]
        qs = self.qs.filter(budget_id__startswith=budget_code)
        qs = depth_by_request(qs, request, budget_code)
        qs = year_by_request(qs, request)
        qs = text_by_request(qs, request)
        qs = distinct_by_request(qs, request)
        qs = limit_by_request(qs, request)
        return qs
    
    @classmethod
    def parent(self, line):
        l = line.containing_line
        parent = []
        while l != None:
            if type(l)==int:
                l = BudgetLine.objects.get(id=l)

            parent.append({ 'budget_id' : l.budget_id, 
                            'title'     : l.title })
            l = l.containing_line
        return parent

        

budget_line_handler= Resource(BudgetLineHandler)

