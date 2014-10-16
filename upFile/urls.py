from django.conf.urls import patterns, include, url
from .views import frametest

urlpatterns = patterns('',
    url(r'^$', frametest, name='frametest'),
    url(r'^uploadduty/$', frametest, name='frametest'),
)
