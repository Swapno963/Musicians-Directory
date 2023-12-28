from django.db import models
from django.contrib.auth.models import User
from musician.models import MusicialModel
# Create your models here.

class AlbumModel(models.Model):
    album_name = models.CharField(max_length=100)
    musician = models.ForeignKey(MusicialModel, on_delete = models.CASCADE, related_name='album')
    release_date = models.DateField()
    rating =  models.CharField(max_length=12)

    def __str__(self) -> str:
        return self.album_name