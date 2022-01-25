from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse
from django.contrib.auth import login, logout

# Create your views here.    
def SignUp_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('HomeHub'))
    else:
        form = UserCreationForm()
    return render(request, 'Invoice/signup.html', {'form': form})


def LogIn_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(reverse('HomeHub'))
    else:
        form = AuthenticationForm()

    return render(request, 'Invoice/login.html', {'form': form})
    
def Logout_view(request):
    logout(request)
    return redirect(reverse('HomeHub')) 