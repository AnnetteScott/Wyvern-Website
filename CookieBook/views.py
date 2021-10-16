from django.shortcuts import render
from . import functions


# Create your views here.
def home(request):
    return render(request, 'CookieBook/home.html')

recipes_cooking = functions.get_recipe_dict("Cooking")

def cooking(request):
    context = {'recipes': recipes_cooking}
    return render(request, 'CookieBook/cooking.html', context)

def cookingRecipe(request, recipename):
    recipe = None
    for pair in recipes_cooking:
        if pair['url'] == str(recipename):
            recipe = pair
    context = {'recipe': recipe}
    return render(request, 'CookieBook/recipe.html', context)


recipes_baking = functions.get_recipe_dict("Baking")
  
def baking(request):
    context = {'recipes': recipes_baking}
    return render(request, 'CookieBook/baking.html', context)

def bakingRecipe(request, recipename):
    recipe = None
    for pair in recipes_baking:
        if pair['url'] == str(recipename):
            recipe = pair
    context = {'recipe': recipe}
    return render(request, 'CookieBook/recipe.html', context)
    
