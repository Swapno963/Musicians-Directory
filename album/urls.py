from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # adding, editing, deleteing
    path('add/', views.AddAlbumCreateView.as_view(),name='add_album'),
    path('edit/<int:id>/', views.EditAlbumCreateView.as_view(),name='edit_album'),
    path('delete/<int:id>/', views.DeleteAlbumView.as_view(),name='delete_album'),
    
]
