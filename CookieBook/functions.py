from django.core.files import File

#Reads the given filename and splits the contents into a list, \n removed
def readfile(filename):
    input_file = open(filename, "r")
    file_contents = input_file.read()
    file_list = file_contents.split("\n")
    input_file.close()
    return file_list


#Takes the raw txt file data and splits it up into seperate recipes - each one contained in a tuple
def split_recipes(raw_data_list):
    recipe_list = []
    current_recipe = []
    for line_to_check in raw_data_list:
        if "Title:" in line_to_check:
            if len(current_recipe) == 0:
                title = line_to_check[7:]
                html_title = "<h1>" + title + "</h1>"
                current_recipe.append(html_title)
            else:
                recipe_list.append(tuple(current_recipe))
                current_recipe = []
                title = line_to_check[7:]
                html_title = "<h1>" + title + "</h1>"
                current_recipe.append(html_title)
        
        if "Ingredients:" in line_to_check:
            html_ingred = "<h2>" + line_to_check + "</h2>"
            current_recipe.append(html_ingred)

        if "-" in line_to_check:
            html_bullet = "<li>" + line_to_check[2:] + "</li>"
            current_recipe.append(html_bullet)
        
        if "Instructions:" in line_to_check:
            html_instruct = "<h2>" + line_to_check + "</h2>"
            current_recipe.append(html_instruct)

    recipe_list.append(tuple(current_recipe))     
    return recipe_list

def get_recipe_titles(recipes_list):
    recipe_titles = []
    for index in range(0, len(recipes_list)):
        recipe_titles.append(recipes_list[index][0][4:-5])
    return recipe_titles


def get_recipe_urls(recipe_titles):
    recipe_url = []
    for title in recipe_titles:
        title = title.lower()
        space = title.find(" ")
        url = title[:space] + title[space + 1:]
        recipe_url.append(url)
    return recipe_url




#Cooking page function
def cooking_page():
    raw_data = readfile("CookieBook/Recipes/Cooking.txt")
    recipes_list = split_recipes(raw_data)
    recipe_titles = get_recipe_titles(recipes_list)
    recipe_urls = get_recipe_urls(recipe_titles)
    print(recipe_urls)



#Baking page function
def baking_page():
    raw_data = readfile("CookieBook/Recipes/Baking.txt")
    recipes_list = split_recipes(raw_data)
    recipe_titles = get_recipe_titles(recipes_list)

    
cooking_page()
