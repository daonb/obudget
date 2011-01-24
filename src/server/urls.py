import os

from django.conf.urls.defaults import *

from budget_lines.handlers import budget_line_handler

urlpatterns = patterns('',
    url(r'^(?P<id>[0-9]+)$', budget_line_handler, name='budget-line-handler'),
    (r'^gwt/(?P<path>.*)$', 'django.views.static.serve', {'document_root':
                                                          os.path.realpath('src/client/war/')}),

)
