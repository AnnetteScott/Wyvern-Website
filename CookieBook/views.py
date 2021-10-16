from django.shortcuts import render
from . import functions


# Create your views here.
def home(request):
    return render(request, 'CookieBook/home.html')

def cooking(request):
    recipes_cooking = functions.get_recipe_dict("Cooking")
    context = {'recipes': recipes_cooking}
    return render(request, 'CookieBook/cooking.html', context)

def cookingRecipe(request, recipename):
    recipes_cooking = functions.get_recipe_dict("Cooking")
    recipe = None
    for pair in recipes_cooking:
        if pair['url'] == str(recipename):
            recipe = pair
    context = {'recipe': recipe}
    return render(request, 'CookieBook/recipe.html', context)

  
def baking(request):
    recipes_baking = functions.get_recipe_dict("Baking")
    context = {'recipes': recipes_baking}
    return render(request, 'CookieBook/baking.html', context)

def bakingRecipe(request, recipename):
    recipes_baking = functions.get_recipe_dict("Baking")
    recipe = None
    for pair in recipes_baking:
        if pair['url'] == str(recipename):
            recipe = pair
    context = {'recipe': recipe}
    return render(request, 'CookieBook/recipe.html', context)
    
