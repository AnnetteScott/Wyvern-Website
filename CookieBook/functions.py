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
    recipe_backgrounds = []
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

        if "Background Image:" in line_to_check:
            semi = line_to_check.find(":")
            image = line_to_check[semi + 2:]
            recipe_backgrounds.append(image)  

    recipe_list.append(tuple(current_recipe))

    recipe_titles = []
    for index in range(0, len(recipe_list)):
        recipe_titles.append(recipe_list[index][0])

    recipe_url = []
    for title in recipe_titles:
        title = title.lower()
        url = title.replace(" ", "-")
        recipe_url.append(url)

    all_info = (recipe_url, recipe_titles, recipe_list, recipe_backgrounds) 

    return all_info


#returns a list with dictionary items for each recipe
def get_recipe_dict(filename):
    all_info = split_recipes(readfile(filename))
    urls = all_info[0]
    titles = all_info[1]
    recipe_list = all_info[2]
    recipe_backgrounds = all_info[3]
    recipe_dict_list = []
    index = 0
    for url_name in urls:
        recipe_dict = {}
        recipe_dict['url'] = url_name
        recipe_dict['title'] = titles[index]
        recipe_dict['first_letter'] = titles[index][0]
        recipe_dict['recipe'] = recipe_list[index][1:]
        recipe_dict['background'] = recipe_backgrounds[index]
        recipe_dict_list.append(recipe_dict)
        index += 1
    
    return recipe_dict_list


def check_alphabet(filename):
    alphabet = ["A", "B", "C", "D", "E", "F", 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    recipe_dict = get_recipe_dict(filename)
    valid_letters = []
    for index in range(len(recipe_dict)):
        for letter in alphabet:
            first_letter = recipe_dict[index]['first_letter']
            if first_letter == letter:
                if letter not in valid_letters:
                    valid_letters.append(letter)
    return valid_letters
