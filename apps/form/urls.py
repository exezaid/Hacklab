from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'apps.form.views.form', name='contact_form'),
    url(r'^sent/$', 'django.views.generic.simple.direct_to_template', {'template': 'contact_form_sent.html'}, name='contact_form_sent'),
)

