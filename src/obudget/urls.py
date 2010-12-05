from django.conf.urls.defaults import *

from obudget import views
from obudget.budget_lines.handlers import budget_line_handler

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.contrib.auth.models import User, Permission
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^obudget/', include('obudget.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^$', views.main),

    # sould be the last line
    url(r'^(?P<id>[0-9]+)$', budget_line_handler, name='budget-line-handler'),
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
