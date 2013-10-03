from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'plants.views.IndexView', name='index'),
    url(r'^plants/', include('plants.urls', namespace="plants")),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^accounts/login/$',  login),
    url(r'^accounts/logout/$', logout),
    url(r'^accounts/', include('accounts.urls', namespace="accounts")),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
