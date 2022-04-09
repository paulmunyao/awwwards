from django.shortcuts import render
from django.contrib.auth import authenticate, login
from  awardpaul.forms import User

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        form = User(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = User()
    return render(request, 'registration/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = User(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = User()
    return render(request, 'registration/register.html', {'form': form})
           
