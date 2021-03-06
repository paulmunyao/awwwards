from django import forms
from django.forms import ModelForm
from .models import Project, Profile, Rate, RATE_CHOICES
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import TextInput, EmailInput


class RegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Username', 'style': 'width:300px;border-radius:25px;'}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'placeholder': 'Email', 'style': 'width: 320px;border-radius:25px;'}))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password', 'style': 'width: 300px;border-radius:25px;'}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Confirm Password', 'style': 'width: 300px;border-radius:25px;'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProjectForm(ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Title', 'style': 'width:300px;border-radius:25px;'}))
    description = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'DEscription', 'style': 'width: 300px;border-radius:25px;'}))
    link = forms.CharField(widget=forms.URLInput(
        attrs={'placeholder': 'Link', 'style': 'width: 300px;border-radius:25px;'}))

    class Meta:
        model = Project
        fields = ['title', 'image', 'description', 'link']


class ProfileForm(ModelForm):
    bio = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Bio', 'style': 'width:300px;border-radius:25px;'}))
    contact = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'contact', 'style': 'width: 300px;border-radius:25px;'}))
    

    class Meta:
        model = Profile
        fields = ['image', 'bio', 'contact']


class RateForm(ModelForm):
    rate = forms.ChoiceField(choices=RATE_CHOICES,
                             widget=forms.Select(), required=True)

    class Meta:
        model = Rate
        fields = ['design', 'usability', 'content']
