from django.conf.urls import patterns, include, url

from views import create_view, check_view


urlpatterns = patterns('',
    url(r'^create/', create_view),
    url(r'^check/(?P<key>\w+)/(?P<code>\w+)/', check_view),
)