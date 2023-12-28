from django import forms 
from .models import MusicialModel

class AlbumForm(forms.ModelForm):
    class Meta:
        model = MusicialModel
        fields = '__all__'