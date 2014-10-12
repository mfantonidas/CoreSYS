from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from ajaxtest import views

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name = 'atest.html')),
    url(r'^input/$', views.input),
)

