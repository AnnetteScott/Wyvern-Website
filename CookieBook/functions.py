#Reads the given filename and splits the contents into a list, \n removed
def readfile(filename):
    file = "CookieBook/Recipes/" + filename + ".txt"
    input_file = open(file, "r")
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
                current_recipe.append(title)
            else:
                recipe_list.append(tuple(current_recipe))
                current_recipe = []
                title = line_to_check[7:]
                current_recipe.append(title)
        
        if "Ingredients:" in line_to_check:
            html_ingred = "<h2>" + line_to_check + "</h2>"
            current_recipe.append(html_ingred)

        if "-" in line_to_check:
            html_bullet = "<li>" + line_to_check[2:] + "</li>"
            current_recipe.append(html_bullet)
            
        if "Cooking Time:" in line_to_check:
            html_time = "<h2>" + line_to_check + "</h2>"
            current_recipe.append(html_time)
        
        if "Instructions:" in line_to_check:
            html_instruct = "<h2>" + line_to_check + "</h2>"
            current_recipe.append(html_instruct)

    recipe_list.append(tuple(current_recipe))     
    return recipe_list

#Gets the recipe titles
def get_recipe_titles(recipes_list):
    recipe_titles = []
    for index in range(0, len(recipes_list)):
        recipe_titles.append(recipes_list[index][0])
    return recipe_titles

#formats the titles into urls
def get_recipe_urls(recipe_titles):
    recipe_url = []
    for title in recipe_titles:
        title = title.lower()
        url = title.replace(" ", "-")
        recipe_url.append(url)
    return recipe_url
    
#returns a list with dictionary items for each recipe
def get_recipe_dict(filename):
    recipes_list = split_recipes(readfile(filename))
    titles = get_recipe_titles(recipes_list)
    recipe_dict_list = []
    urls = get_recipe_urls(titles)
    index = 0
    for url_name in urls:
        recipe_dict = {}
        recipe_dict['url'] = url_name
        recipe_dict['title'] = titles[index]
        recipe_dict['recipe'] = recipes_list[index][1:]
        recipe_dict_list.append(recipe_dict)
        index += 1
    return recipe_dict_list
