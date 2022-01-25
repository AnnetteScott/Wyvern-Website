from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse
from django.contrib.auth import login, logout

# Create your views here.
def home(request):
    return render(request, 'Invoice/home.html')
    
def userHome(request, user_name):

    return render(request, 'Invoice/home.html')