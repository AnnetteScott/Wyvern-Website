def readfile(filename):
    input_file = open(filename, "r")
    file_contents = input_file.read()
    file_list = file_contents.split("\n")
    input_file.close()
    return file_list


def split_recipes(recipe_list):
    title = ""
    ingred = []
    cooking_time = ""
    instructions = []
    recipe = []
    for index in range(0, len(recipe_list)):
        if "Title:" in recipe_list[index]:
            semi = recipe_list[index].find(":") + 1
            title = recipe_list[index][semi:]
            title = title.strip()
            recipe.append(title)
        elif "Ingredients:" in recipe_list[index]:
            ingredient_index = index  + 1
            ingredient_line = recipe_list[ingredient_index]
            while "-" in ingredient_line:
                dash = recipe_list[ingredient_index].find("-") + 1
                ingredient = recipe_list[ingredient_index][dash:]
                ingredient = ingredient.strip()               
                ingred.append(ingredient)
            recipe.append(ingred)
        elif "Cooking Time:" in recipe_list[index]:
            semi = recipe_list[index].find(":") + 1
            cooking_time = recipe_list[index][semi:]
            cooking_time = cooking_time.strip()
            recipe.append(cooking_time)
        elif "Instructions:" in recipe_list[index]:
            instructions_index = index  + 1
            instructions_line = recipe_list[instructions_index]
            while "-" in instructions_line:
                dash = recipe_list[instructions_index].find("-") + 1
                instruction = recipe_list[instructions_index][dash:]
                instruction = instruction.strip()               
                instructions.append(instruction)
            recipe.append(instructions)
    

