from django.conf.urls import patterns, include, url
from propertys import urls as propertysurl
from django.contrib import admin
admin.autodiscover()
#import pdb;pdb.set_trace()
urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'demo.views.home', name='home'),
    # url(r'^demo/', include('demo.foo.urls')),
    url(r'',include(propertysurl)),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)