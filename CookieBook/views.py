from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'CookieBook/home.html')

def cooking(request):
    return render(request, 'CookieBook/cooking.html')
    
def baking(request):
    return render(request, 'CookieBook/baking.html')