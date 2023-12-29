from django.shortcuts import render

# Create your views here.
from . import models
from . import forms
from django.views.generic import DetailView
# for view
from django.utils.decorators import method_decorator
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView,UpdateView,DeleteView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy



# add post useing class based view
@method_decorator(login_required, name='dispatch')
class AddAlbumCreateView(SuccessMessageMixin,CreateView):
    model = models.AlbumModel
    form_class = forms.AlbumForm
    template_name = 'add_album.html'
    success_url = '/'
    success_message = 'Album Created Successfully'
    def form_valid(self, form):
        # form.instance.author = self.request.user
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class EditAlbumCreateView(SuccessMessageMixin, UpdateView):
    model =models.AlbumModel
    form_class = forms.AlbumForm
    template_name = 'add_album.html'
    pk_url_kwarg = 'id'
    success_message = 'Album Edited Successfully'
    success_url = '/'



@method_decorator(login_required, name='dispatch')
class DeleteAlbumView(SuccessMessageMixin, DeleteView):
    model = models.MusicialModel
    template_name = 'delete.html'
    success_message = 'Post Deleted Successfully'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id'
    
