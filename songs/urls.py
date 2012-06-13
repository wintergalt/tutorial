from django.conf.urls import patterns, include, url

urlpatterns = patterns('songs.views',
    url(r'^$', 'index'),
    url(r'^new-artist-form$', 'new_artist_form'),
    url(r'^new-song-form$', 'new_song_form'),
    url(r'^new-song-submit$', 'new_song_submit'),
    url(r'^song/(?P<song_id>\d+)/$', 'song_detail'),
)

