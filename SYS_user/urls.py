from django.conf.urls import patterns, url
from django.contrib.auth.views import login, logout
from SYS_user import views

urlpatterns = patterns('',
    url(r'^$', views.login),
    url(r'^login/$', views.login),
    url(r'^regist/$', views.regist, name='regist'),
    url(r'^index/$', views.index, name='index'),
    url(r'^logout/$', views.logout, name='logout'),
)