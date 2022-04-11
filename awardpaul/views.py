from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, ProjectForm
from .models import Project, Profile, Rate

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
    context = {
        'user': request.user,
    }
    return render(request, 'profile.html', context)


def post(request):
    context = {
        'user': request.user,
    }
    form = ProjectForm()
    return render(request, 'post.html', context, {'form': form})


@login_required(login_url='registration/login/')
def display(request, id):
    post = Project.objects.all()
    return render(request, 'display.html', {'post': post})


def rate(request, id):
    context = {
        'user': request.user,
    }
    post = Project.objects.get(id=id)

    if request.method == 'POST':
        form = Rate(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.user = User
            rate.project = Project
            rate.save()
            design = form.cleaned_data['design']
            usability = form.cleaned_data['usability']
            content = form.cleaned_data['content']
            overall = (design + usability + content) / 3
            rate = Rate(user=request.user, project=post, design=design,
                        usability=usability, content=content, overall=overall)
            rate.save()
            return redirect('profile')
    return render(request, 'rate.html', context, {'post': post})
