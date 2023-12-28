from django.shortcuts import render
from album.models import AlbumModel
from musician.models import MusicialModel



        
def home(request):
    musician = MusicialModel.objects.all()
    # album = AlbumModel.objects.filter(musician = musician)
    # print(data)
    return render(request, 'home.html',{'data':musician})

def home2(request):
    album = AlbumModel.objects.all()
    return render(request, 'home_2.html',{'data':album})