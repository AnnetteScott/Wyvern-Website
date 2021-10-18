from django.shortcuts import render
from . import functions
recipe_type_list = functions.get_all_recipe_file_names()
recipes_list = []
valid_letters = []

# Create your views here.
def home(request):
    global recipe_type_list 
    recipe_type_list = functions.get_all_recipe_file_names()
    context = {'recipe_type': recipe_type_list} 
    return render(request, 'CookieBook/home.html', context)

def recipeList(request, the_type_of_recipe):
    type_of_recipe = None
    for recipe_type in recipe_type_list:
        if recipe_type['recipeType'] == str(the_type_of_recipe):
            type_of_recipe = recipe_type
    filename = type_of_recipe["UpperCase"]
    global recipes_list
    global valid_letters
    recipes_list = functions.get_recipe_dict(filename)
    valid_letters = functions.check_alphabet(filename)
    context = {'recipes': recipes_list, 'alphabet': valid_letters}
    return render(request, 'CookieBook/table_of_contents.html', context)


def recipePage(request, the_type_of_recipe, recipename):
    for pair in recipes_list:
        if pair['url'] == str(recipename):
            recipe = pair
    context = {'recipe': recipe}
    return render(request, 'CookieBook/recipe.html', context)

