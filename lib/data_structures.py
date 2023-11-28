spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    # use list comprehension to extract the 
    # name from each dictionary in the list
    return [food['name'] for food in spicy_foods]
pass

def get_spiciest_foods(spicy_foods):
    # use list comprehension to filter out foods 
    # with heat_level greater than 5
    return [food for food in spicy_foods 
            if food['heat_level'] > 5]
pass

def print_spicy_foods(spicy_foods):
    # loop through each food in the list
    for food in spicy_foods:
    # print the food's data
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")
    pass

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    # use next() with a generator to find the first 
    # food that matches the specified cuisine
    return next((food for food in spicy_foods if food['cuisine'] == cuisine), None)
pass

def print_spiciest_foods(spicy_foods):
    # get the spiciest foods using the 
    # get_spiciest_foods function
    spiciest_foods = get_spiciest_foods(spicy_foods)
    # print each spicy food using the 
    # print_spicy_foods function
    print_spicy_foods(spiciest_foods)
    pass

def get_average_heat_level(spicy_foods):
    # calculate the total heat level by summing 
    # up the heat_level of each food
    total_heat = sum(food['heat_level'] for food in spicy_foods)
    # calculate the average heat level by dividing the total heat by the sum of foods
    average_heat = total_heat / len(spicy_foods)
    return average_heat
pass

def create_spicy_food(spicy_foods, spicy_food):
    # add the new food to the list
    spicy_foods.append(spicy_food)
    # return the updated list
    return spicy_foods
    pass
