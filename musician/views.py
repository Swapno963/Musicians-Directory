from django.shortcuts import render,redirect
from . import forms 
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


# for addint editing and deleting
from django.utils.decorators import method_decorator
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView,UpdateView,DeleteView
from . import models





# Create your views here.
def register(request):
    if request.method == 'POST':
        register_form = forms.RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Register Successfully.')
            return redirect('home')
    else:
        register_form = forms.RegistrationForm()
    return render(request, 'register.html',{'form':register_form, 'type':'Register'})

class UserLoginView(LoginView):
    template_name = 'register.html'
    success_url = reverse_lazy('musician:user_profile')

    def form_valid(self,form):
        messages.success(self.request, 'Logged in Successful')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request, 'Logged in Information Incorrect')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context
    
@login_required
def user_profile(request):
    return render(request, 'user_profile.html',{'user':request.user})

def user_logout(request):
    logout(request)
    return redirect('login')

# adding and editing
# add post useing class based view
@method_decorator(login_required, name='dispatch')
class AddMusicianCreateView(SuccessMessageMixin,CreateView):
    model = models.MusicialModel
    form_class = forms.MusicianForm
    template_name = 'add_musician.html'
    success_url = '/musician/profile'
    success_message = 'Musician Created Successfully'
    def form_valid(self, form):
        # form.instance.author = self.request.user
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class EditMusicianCreateView(SuccessMessageMixin, UpdateView):
    model =models.MusicialModel
    form_class = forms.MusicianForm
    template_name = 'add_musician.html'
    pk_url_kwarg = 'id'
    success_message = 'Post Edited Successfully'
    success_url = '/musician/profile'



@method_decorator(login_required, name='dispatch')
class DeleteMusicianView(SuccessMessageMixin, DeleteView):
    model = models.MusicialModel
    template_name = 'delete.html'
    success_message = 'Post Deleted Successfully'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id'
