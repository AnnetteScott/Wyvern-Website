from django.shortcuts import render
from . import functions
from .models import Recipe


# Create your views here.
def home(request):
    current_types = []
    recipe_list = list(Recipe.objects.values_list('tag', flat=True))
    recipe_type_list = []
    for type in recipe_list:
        a_dict = {}
        if type not in current_types:
            url = type.lower()
            a_dict['recipeType'] = url
            a_dict['UpperCase'] = type
            recipe_type_list.append(a_dict)
            current_types.append(type)

    context = {'recipe_type': recipe_type_list} 
    return render(request, 'CookieBook/home.html', context)

def recipeList(request, the_type_of_recipe):
    list_ids = list(Recipe.objects.values_list('id', flat=True).order_by('id'))
    recipe_page_list = []
    valid_letters = []
    for index in range(len(list_ids)):
        recipe_obj = Recipe.objects.get(id=list_ids[index])
        if recipe_obj.tag.lower() == str(the_type_of_recipe):
            first_letter = recipe_obj.title[0]
            recipe_page_list.append(recipe_obj)
            valid_letters.append(str(recipe_obj.title[0]))
  
    valid_letters.sort()
    context = {'alphabet': valid_letters, 'recipe': recipe_page_list}
    return render(request, 'CookieBook/table_of_contents.html', context)


def recipePage(request, the_type_of_recipe, recipename):
    context = {}
    return render(request, 'CookieBook/recipe.html', context)

