from django.forms import ModelForm
from songs.models import Song

class SongForm(ModelForm):
    class Meta:
        model = Song