from django.conf.urls import patterns, include, url

urlpatterns = patterns('songs.views',
    url(r'^$', 'index'),
)

