from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('post/', views.post, name='post'), 
    path('profile/', views.profile, name='profile'),
    path('display/', views.display, name='display'),
    
]