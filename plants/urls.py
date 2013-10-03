'''
Created on 15 sep 2013

@author: balp
'''

from django.conf.urls import patterns, url

from plants import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
)
