def readfile(filename):
    input_file = open(filename, "r")
    file_contents = input_file.read()
    file_list = file_contents.split("\n")
    input_file.close()
    return file_list


def split_recipes(recipe_raw):
    title = ""
    ingred = []
    cooking_time = ""
    instructions = []
    recipe = []
    recipe_list = []
    for index in range(0, len(recipe_raw)):
        if "Title:" in recipe_raw[index]:
            semi = recipe_raw[index].find(":") + 1
            title = recipe_raw[index][semi:]
            title = title.strip()
            recipe.append(title)
        elif "Ingredients:" in recipe_raw[index]:
            ingredient_index = index  + 1
            ingredient_line = recipe_raw[ingredient_index]
            while "-" in ingredient_line:
                dash = recipe_raw[ingredient_index].find("-") + 1
                ingredient = recipe_raw[ingredient_index][dash:]
                ingredient = ingredient.strip()               
                ingred.append(ingredient)
            recipe.append(ingred)
        elif "Cooking Time:" in recipe_raw[index]:
            semi = recipe_raw[index].find(":") + 1
            cooking_time = recipe_raw[index][semi:]
            cooking_time = cooking_time.strip()
            recipe.append(cooking_time)
        elif "Instructions:" in recipe_raw[index]:
            instructions_index = index  + 1
            instructions_line = recipe_raw[instructions_index]
            while "-" in instructions_line:
                dash = recipe_raw[instructions_index].find("-") + 1
                instruction = recipe_raw[instructions_index][dash:]
                instruction = instruction.strip()               
                instructions.append(instruction)
            recipe.append(instructions)
        recipe_tuple = tuple(recipe)
        recipe_list.append(recipe_tuple)
    return recipe_list

    
    

