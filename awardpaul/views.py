from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, ProjectForm
from .models import Project

# Create your views here.


def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})


def post(request):
    form = ProjectForm()
    return render(request, 'post.html', {'form': form})

@login_required(login_url='registration/login/')
def display(request):
    post = Project.objects.all()
    return render(request, 'display.html', {'post': post})  

def logout_view(request):
    logout(request)


      

