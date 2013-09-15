'''
Created on 15 sep 2013

@author: balp
'''

from django.conf.urls import patterns, url

from accounts import views

urlpatterns = patterns('',
    url(r'^profile/$', views.profile, name='profile'),
)
