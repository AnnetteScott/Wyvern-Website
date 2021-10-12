from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'CookieBook/home.html')

def cooking(request):
    return render(request, 'CookieBook/cooking.html')
    
def cookingRecipe(request, recipename):
    return render(request, 'CookieBook/recipe.html')
    
def baking(request):
    return render(request, 'CookieBook/baking.html')