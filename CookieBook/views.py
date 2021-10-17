from django.shortcuts import render
from . import functions
recipe_type_list = [
    {"recipeType": "cooking", 'UpperCase': "Cooking"},
    {"recipeType": "baking", 'UpperCase': "Baking"}
]

# Create your views here.
def home(request):
    context = {'recipe_type': recipe_type_list} 
    return render(request, 'CookieBook/home.html', context)

def recipeList(request, the_type_of_recipe):
    type_of_recipe = None
    for recipe_type in recipe_type_list:
        if recipe_type['recipeType'] == str(the_type_of_recipe):
            type_of_recipe = recipe_type
    filename = type_of_recipe["UpperCase"]
    recipes_list = functions.get_recipe_dict(filename)
    valid_letters = functions.check_alphabet(filename)
    context = {'recipes': recipes_list, 'alphabet': valid_letters}
    return render(request, 'CookieBook/table_of_contents.html', context)


def recipePage(request, the_type_of_recipe, recipename):
    type_recipe = None
    for recipeTYPE in recipe_type_list:
        if recipeTYPE['recipeType'] == str(the_type_of_recipe):
            type_recipe = recipeTYPE
    filename = type_recipe["UpperCase"]
    recipes_list = functions.get_recipe_dict(filename)
    for pair in recipes_list:
        if pair['url'] == str(recipename):
            recipe = pair
    context = {'recipe': recipe, 'pages': type_recipe}
    return render(request, 'CookieBook/recipe.html', context)

