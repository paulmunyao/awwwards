from django.shortcuts import render
from  awardpaul.forms import User

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    form = User()
    return render(request, 'registration/login.html', {'form': form})

    

def register(request):
    return render(request, 'registration/register.html')        
