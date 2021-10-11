#Reads the given filename and splits the contents into a list, \n removed
def readfile(filename):
    input_file = open(filename, "r")
    file_contents = input_file.read()
    file_list = file_contents.split("\n")
    input_file.close()
    return file_list


#Takes the raw txt file data and splits it up into seperate recipes - each one contained in a tuple
def split_recipes(recipe_raw):
    title = ""
    ingred = []
    cooking_time = ""
    instructions = []
    recipe = []
    recipe_list = []
    for index in range(0, len(recipe_raw)):
        if "Title:" in recipe_raw[index]:
            if len(recipe) != 0:
                recipe_tuple = tuple(recipe)
                recipe_list.append(recipe_tuple)
                recipe = []
            semi = recipe_raw[index].find(":") + 1
            title = recipe_raw[index][semi:]
            title = title.strip()
            recipe.append(title)
        elif "Ingredients:" in recipe_raw[index]:
            ingredient_index = index  + 1
            ingredient_line = recipe_raw[ingredient_index]
            while "-" in ingredient_line:
                dash = ingredient_line.find("-")
                ingredient = ingredient_line[dash + 1:]
                ingredient = ingredient.strip()               
                ingred.append(ingredient)
                ingredient_index += 1
                ingredient_line = recipe_raw[ingredient_index]
            recipe.append(ingred)
        elif "Cooking Time:" in recipe_raw[index]:
            semi = recipe_raw[index].find(":") + 1
            cooking_time = recipe_raw[index][semi:]
            cooking_time = cooking_time.strip()
            recipe.append(cooking_time)
        elif "Instructions:" in recipe_raw[index]:
            instructions_index = index  + 1
            instructions_line = recipe_raw[instructions_index]
            while "-" in instructions_line and instructions_index < len(recipe_raw):
                instructions_line = recipe_raw[instructions_index]
                dash = instructions_line.find("-")
                instruction = instructions_line[dash + 1:]
                instruction = instruction.strip()               
                instructions.append(instruction)
                instructions_index += 1
            recipe.append(instructions)
    if len(recipe) != 0:
        recipe_tuple = tuple(recipe)
        recipe_list.append(recipe_tuple)
        recipe = []
    return recipe_list

#Cooking page function
def cooking_page():
    raw_data = readfile("Cooking.txt")
    recipes = split_recipes(raw_data)

#Baking page function
def baking_page():
    raw_data = readfile("Baking.txt")
    recipes = split_recipes(raw_data)

    
    

