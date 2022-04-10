from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from .forms import RegisterForm,ProjectForm

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
    if request.method == 'POST':
        form = ProjectForm()
        if form.is_valid():
            form.save()
            return redirect('display')
    else:
        form = ProjectForm()
    return render(request,'post.html',{'form':form}) 

def display(request):
    posts = ProjectForm.objects.all()
    return render(request, 'display.html')    

