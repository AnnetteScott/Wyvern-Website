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
    modified_data = raw_data_list
    recipe_list = []
    current_recipe = []
    index_end = 0
    for line_to_check in raw_data_list:

        if "Title:" in line_to_check:
            if len(current_recipe) != 0:
                recipe_list.append(tuple(current_recipe))
                current_recipe = []
                modified_data = raw_data_list[index_end + 1:]
            title = line_to_check[6:]
            title = title.strip()
            current_recipe.append(title)
        
        if "Ingredients:" in line_to_check:
            index_start = (modified_data.index("Ingredients:")) + 1
            index_end = raw_data_list[index_start]
            end_line = raw_data_list[index_end]
            ingredients = []
    
            while "Cooking Time:" not in end_line:
                index_end += 1
                end_line = raw_data_list[index_end]

            while index_start <= index_end:
                ingredients.append(raw_data_list[index_start][2:])
                index_start += 1
            
            current_recipe.append(ingredients)
        
        if "Cooking Time:" in line_to_check:
            cooking_time = line_to_check[14:]
            current_recipe.append(cooking_time)
        
        if "Instructions:" in line_to_check:
            index_start = (modified_data.index("Instructions:")) + 1
            index_end = raw_data_list[index_start]
            end_line = raw_data_list[index_end]
            instructions = []
    
            while "Title: " not in end_line:
                index_end += 1
                end_line = raw_data_list[index_end]

            while index_start <= index_end:
                instructions.append(raw_data_list[index_start][2:])
                index_start += 1
            
            current_recipe.append(instructions)
    
    recipe_list.append(tuple(current_recipe))
    current_recipe = []
    modified_data = raw_data_list[index_end + 1:]
    return recipe_list

#Returns a dictionary with title as key
def dict_recipe(recipes):
    recipe_dict = {}
    for index in range(0, len(recipes)):
        title = recipes[index][0]
        recipe_dict[title] = recipes[index][1:]
    return recipe_dict

#Returns a list of titles
def titles(recipes):
    recipe_titles = []
    for index in range(0, len(recipes)):
        title = recipes[index][0]
        recipe_titles.append(title)
    return recipe_titles


#Cooking page function
def cooking_page():
    raw_data = readfile("CookieBook/Recipes/Cooking.txt")
    recipes_list = split_recipes(raw_data)
    recipes_dict = dict_recipe(recipes_list)
    recipe_titles = titles(recipes_list)
  #  print(recipe_titles)
   # print(recipes_dict)


#Baking page function
def baking_page():
    raw_data = readfile("CookieBook/Recipes/Baking.txt")
    recipes_list = split_recipes(raw_data)
    recipes_dict = dict_recipe(recipes_list)
    recipe_titles = titles(recipes_list)
    
cooking_page()
