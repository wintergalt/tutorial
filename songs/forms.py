from django.forms import ModelForm
from songs.models import Song, Artist

class SongForm(ModelForm):
    class Meta:
        model = Song
        
class ArtistForm(ModelForm):
    class Meta:
        model = Artist