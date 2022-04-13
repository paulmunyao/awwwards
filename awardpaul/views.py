from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, RegisterForm, ProjectForm, ProfileForm, RateForm, RATE_CHOICES
from .models import Project, Profile, Rate
from django.template import loader

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


def profile(request):
    form = ProfileForm()
    return render(request, 'profile.html', {'form': form})


def post(request):
    form = ProjectForm()
    return render(request, 'post.html',  {'form': form})


@login_required(login_url='registration/login/')
def display(request):
    post = Project.objects.all()
    return render(request, 'display.html', {'post': post})


def rate(request, id):
    current_user = request.user
    project = Project.objects.get(id=id)
    rates = Rate.objects.filter(project=project, user=current_user)
    if request.method == 'POST':
        form = RateForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.project = Project.objects.get(id=id)
            rate.user = request.user
            rate.save()
            return redirect('display')
    else:
        form = RateForm()
    return render(request, 'rate.html', {'form': form, 'rate': RATE_CHOICES, 'project': project, 'rates': rates})
