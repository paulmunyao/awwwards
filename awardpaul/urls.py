from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('display/', views.login, name='display'),
    path('post/', views.post, name='post'), 
]