from django import forms 
from .models import AlbumModel
RATING_CHOICE = (
    ('1','one'),
    ('2','two'),
    ('3','three'),
    ('4','four'),
    ('5','five'),
)
class AlbumForm(forms.ModelForm):
    rating = forms.MultipleChoiceField(choices = RATING_CHOICE) 

    class Meta:
        model = AlbumModel
        fields = '__all__'