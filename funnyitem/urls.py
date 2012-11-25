from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from funnyitemposts.views import *

urlpatterns = patterns('',
    ('^$', home), #added
    (r'^funnyitempost/(?P<funnyitempost_id>\d+)/$',funnyitempost_specific), #added
    # Examples:
    # url(r'^$', 'funnyitem.views.home', name='home'),
    # url(r'^funnyitem/', include('funnyitem.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
