from django import forms
from django.forms import ModelForm
from .models import Project, Profile, Rate, RATE_CHOICES
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'image', 'description', 'link']  

class RateForm(ModelForm):
    class Meta:
        model = Rate
        fields = ['design', 'usability', 'content']        