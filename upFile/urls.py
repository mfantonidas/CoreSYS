from django.conf.urls import patterns, include, url
from .views import frametest, ftest, upfile
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^$', frametest, name='frametest'),
    url(r'^uploadduty/$', frametest, name='frametest'),
    #url(r'^ftest/$', TemplateView.as_view(template_name = 'ftest.html')),
    url(r'^ftest/$', upfile),
)
