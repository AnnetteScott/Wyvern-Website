from django.shortcuts import render, redirect
from django.urls import reverse

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        url = "/invoice/" + request.user.username + "/"
        return redirect(url)
    else:
        return render(request, 'Invoice/home.html')
    
def userHome(request, user_name):

    return render(request, 'Invoice/userHome.html')