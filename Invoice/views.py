from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
    return render(request, 'Invoice/home.html')
    
def SignUp(request):
    form = UserCreationForm()
    return render(request, 'Invoice/signup.html', {'form': form})
    
def SignIn(request):
    return render(request, 'Invoice/signin.html')