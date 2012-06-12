from django.conf.urls import patterns, include, url
from django.views.static import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

print 'MEDIA_ROOT: ', settings.MEDIA_ROOT
print 'MEDIA_URL: ', settings.MEDIA_URL

urlpatterns = patterns('',
    url(r'^polls/', include('polls.urls')),
    url(r'^songs/', include('songs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

