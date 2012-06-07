from songs.models import Song, Artist
from django.shortcuts import render_to_response
#import logging

#logger = logging.get_logger(__name__)

def index(request):
	#logger.error('Inside index view')
	latest_song_list = Song.objects.all().order_by('-created')[:5]
	#logger.error('latest_songs_list size: ' + latest_songs_list.size)
	return render_to_response('songs/index.html', {'latest_song_list': latest_song_list})