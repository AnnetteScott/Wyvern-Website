from django.shortcuts import render
from .models import Recipe

recipe_page_list = []

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
    global recipe_page_list
    recipe_page_list = []
    valid_letters = []
    for index in range(len(list_ids)):
        recipe_obj = Recipe.objects.get(id=list_ids[index])
        if recipe_obj.tag.lower() == str(the_type_of_recipe):
            first_letter = recipe_obj.title[0]
            recipe_page_list.append(recipe_obj)
            valid_letters.append(str(first_letter))
            print(recipe_obj.img_initial)
            print("line before this")
  
    valid_letters.sort()
    context = {'alphabet': valid_letters, 'recipe': recipe_page_list}
    return render(request, 'CookieBook/table_of_contents.html', context)


def recipePage(request, the_type_of_recipe, recipeurl):
    recipe_page_data = None
    list_ids = list(Recipe.objects.values_list('id', flat=True).order_by('id'))
    for index in range(len(list_ids)):
        recipe_obj = Recipe.objects.get(id=list_ids[index])
        url = ''
        if recipe_obj.url == '' or recipe_obj.url == 'null':
            url = (recipe_obj.title.replace(' ', '-')).lower()
        if recipe_obj.url == recipeurl or url == recipeurl:
            recipe_page_data = recipe_obj
            break
    context = {'recipe': recipe_page_data}
    return render(request, 'CookieBook/recipe.html', context)

