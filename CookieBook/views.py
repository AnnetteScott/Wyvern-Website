from django.shortcuts import render
from . import functions


# Create your views here.
def home(request):
    return render(request, 'CookieBook/home.html')



# Create your views here.
def home(request):
    return render(request, 'CookieBook/home.html')

recipes = functions.get_recipe_dict_cooking()

def cooking(request):
    context = {'recipes': recipes}
    return render(request, 'CookieBook/cooking.html', context)

def cookingRecipe(request, recipename):
    recipe = None
    for pair in recipes:
        if pair['url'] == str(recipename):
            recipe = pair
    context = {'recipe': recipe}
    return render(request, 'CookieBook/recipe.html', context)
    
def baking(request):
    return render(request, 'CookieBook/baking.html')