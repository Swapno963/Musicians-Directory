from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.UserLoginView.as_view(),name='login'),
    path('register/', views.register,name='register'),
    path('profile/', views.user_profile, name='profile'),
    path('logout/', views.user_logout,name='logout'),

    # adding, editing, deleteing
    path('add/', views.AddMusicianCreateView.as_view(),name='add_musician'),
    path('edit/<int:id>/', views.EditMusicianCreateView.as_view(),name='edit_musician'),
    path('delete/<int:id>/', views.DeleteMusicianView.as_view(),name='delete_musician'),
    
]
