from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'folik.views.home_page', name='home'),
    url(r'^kontakt/$', 'folik.views.kontakt_page', name='kontakt'),
    url(r'^tehtud_t88d/$', 'folik.views.works_page', name='works'),
    url(r'^oskused/$', 'folik.views.oskused_page', name='oskused'),
)
