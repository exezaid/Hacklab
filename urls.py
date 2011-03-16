from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
from django.views.generic.simple import direct_to_template

from feeds import LatestEntries

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url':'/media/img/favicon.ico'}),
    (r'^robots\.txt$', direct_to_template, {'template':'robots.txt', 'mimetype':'text/plain'}),
    (r'^about/', direct_to_template, {'template':'about.html'}, 'default'),
    (r'^recommend/', direct_to_template, {'template':'recommend.html'}, 'recommend'),
    (r'^feeds/latest/$', LatestEntries()),

    url(r'^(?P<slug>[-\w]+)/$', 'apps.blog.views.post',   name='post'),
    (r'^comments/', include('django.contrib.comments.urls')),
    url(r'^$', 'apps.blog.views.main', name='main'),
)

import sys, os
from django.conf import settings
if 'runserver' in sys.argv or 'runserver_plus':
    urlpatterns = patterns('', url(r'^media/(.*)$', 'django.views.static.serve',
        kwargs={'document_root': settings.MEDIA_ROOT}),
    ) + urlpatterns