from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse

# Create your views here.
def home(request):
    return render(request, 'Invoice/home.html')
    
def SignUp(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            #log the user in
            return redirect(reverse('Invoice'))
    else:
        form = UserCreationForm()
    return render(request, 'Invoice/signup.html', {'form': form})


def SignIn(request):
    return render(request, 'Invoice/signin.html')