from songs.models import Song, Artist
from django.shortcuts import render_to_response

def index(request):
	latest_song_list = Song.objects.all().order_by('-created')[:5]
	return render_to_response('songs/index.html', {'latest_song_list': latest_song_list})