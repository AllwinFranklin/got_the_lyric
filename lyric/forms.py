from .models import Lyric
from django.forms import ModelForm

class LyricForm(ModelForm):
    class Meta:
        model = Lyric
        fields = ['author', 'title', 'key', 'lyrics']