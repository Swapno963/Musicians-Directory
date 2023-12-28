from django.shortcuts import render
from album.models import AlbumModel
from musician.models import MusicialModel
from django.views.generic import DetailView
from album.models import AlbumModel
from album.forms import AlbumForm
# class DetailPostView(DetailView):
#     model = AlbumModel
#     template_name = 'home.html'

#     def post(self, request, *args, **kwargs):
#         comment_form = AlbumForm(self.request.POST)
#         post = self.get_object()
#         if comment_form.is_valid():
#             new_comment = comment_form.save(commit=False)
#             new_comment.post = post
#             new_comment.save()
#         return self.get(request, *args, **kwargs)
     
            
#     def get_context_data(self, **kwargs):
        
#         context = super().get_context_data(**kwargs)
#         post = self.object 
#         comments = post.comments.all()
#         comment_form = forms.CommentForm()
           

#         context['comments'] = comments
#         context['comment_form'] = comment_form
#         return context


        
def home(request):
    musician = MusicialModel.objects.all()
    # album = AlbumModel.objects.filter(musician = musician)
    # print(data)
    return render(request, 'home.html',{'data':musician})