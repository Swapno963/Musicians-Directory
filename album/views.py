from django.shortcuts import render

# Create your views here.
from . import models
from . import forms
from django.views.generic import DetailView

# class DetailPostView(DetailView):
#     model = models.Post
#     template_name = 'post_detail.html'

#     def post(self, request, *args, **kwargs):
#         comment_form = forms.CommentForm(self.request.POST)
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

