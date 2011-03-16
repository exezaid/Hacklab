from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'apps.blog.views.main', name='main'),
    url(r'^blog/(?P<slug>[-\w]+)/$', 'apps.blog.views.post',   name='post'),
    url(r'^category/(?P<object_pk>[0-9]+)/$', 'apps.blog.views.category', name='blog_category'),
)
