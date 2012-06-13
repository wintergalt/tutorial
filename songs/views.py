from songs.models import Song, Artist
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from songs.forms import SongForm
from django.http import HttpResponseRedirect
from django.contrib import messages

def index(request):
    latest_song_list = Song.objects.all().order_by('-created')[:5]
    return render_to_response('songs/index.html', 
        {'latest_song_list': latest_song_list},
        context_instance=RequestContext(request))

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
            messages.add_message(request, messages.INFO, 'Song added successfully')
            return index(request)

    else:
        form = SongForm()

    return render_to_response('songs/new_song_form.html',
        {'form': form},
        context_instance=RequestContext(request))

def song_detail(request, song_id):
    try:
        song = get_object_or_404(Song, pk=song_id)
    except Song.DoesNotExist:
        raise Http404
    return render_to_response('songs/song_detail.html',
        {'song': song},
        context_instance=RequestContext(request))
    