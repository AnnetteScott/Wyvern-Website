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
                recipe_list.append(current_recipe)
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

    recipe_list.append(current_recipe)
       
    return recipe_list



#Cooking page function
def cooking_page():
    raw_data = readfile("CookieBook/Recipes/Cooking.txt")
    recipes_list = split_recipes(raw_data)
    print(recipes_list)



#Baking page function
def baking_page():
    raw_data = readfile("CookieBook/Recipes/Baking.txt")
    recipes_list = split_recipes(raw_data)

    
cooking_page()
