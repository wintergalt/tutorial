from songs.models import Song, Artist
from django.shortcuts import render_to_response
from django.template import RequestContext
from songs.forms import SongForm
from django.http import HttpResponseRedirect

def index(request, msg=None):
    latest_song_list = Song.objects.all().order_by('-created')[:5]
    request_dict = {'latest_song_list': latest_song_list}
    if msg: request_dict['message'] = msg
    return render_to_response('songs/index.html', 
        context_instance=RequestContext(request, request_dict))

def new_song_form(request):
    form = SongForm()
    return render_to_response('songs/new_song_form.html', 
        { 'form': form },
        context_instance=RequestContext(request))

def new_song_submit(request):
    if request.method == 'POST':
        form = SongForm(request.POST)
        if form.is_valid():
            # Process form data
            form.save()
            return index(request, 'Song added successfully')

    else:
        form = SongForm()

    return render_to_response('songs/new_song_form.html',
        {'form': form},
        context_instance=RequestContext(request))

