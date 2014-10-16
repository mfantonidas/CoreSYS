from django.conf.urls import patterns, include, url

import xadmin
xadmin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CoreSYS.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^xadmin/', include(xadmin.site.urls)),
    url(r'core_user/', include('SYS_user.urls')),
    url(r'api/', include('api_auth.urls', namespace='rest_framework')),
    url(r'ajaxtest/', include('ajaxtest.urls')),
    url(r'core_file/', include('upFile.urls'), name='core_file'),
)
