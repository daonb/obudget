
import os

from django.conf.urls.defaults import *
from django.views.decorators.cache import cache_page

from budget_lines.handlers import budget_line_handler

urlpatterns = patterns('',
    url(r'^(?P<id>[0-9]+)$', cache_page(budget_line_handler, 30*60), name='budget-line-handler'),
    (r'^gwt/(?P<path>.*)$', 'django.views.static.serve', {'document_root':
                                                          os.path.realpath('src/client/war/')}),

)
