from django.conf.urls.defaults import *

urlpatterns = patterns('',

    # filebrowser urls
    url(r'^browse/$', 'apps.filebrowser.views.browse', name="fb_browse"),
    url(r'^mkdir/', 'apps.filebrowser.views.mkdir', name="fb_mkdir"),
    url(r'^upload/', 'apps.filebrowser.views.upload', name="fb_upload"),
    url(r'^rename/$', 'apps.filebrowser.views.rename', name="fb_rename"),
    url(r'^delete/$', 'apps.filebrowser.views.delete', name="fb_delete"),
    url(r'^versions/$', 'apps.filebrowser.views.versions', name="fb_versions"),

    url(r'^check_file/$', 'apps.filebrowser.views._check_file', name="fb_check"),
    url(r'^upload_file/$', 'apps.filebrowser.views._upload_file', name="fb_do_upload"),

)

