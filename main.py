# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

meals = [
    {"pizza": ["flour", "yeast", "pizza sauce", "shredded mozzarella", "pepperoni"]},
    {"ham and biscuits": ["grands rolls", "ham", "loaded potato soup", "smoked gouda", "frozen peas", ]},
    {"bacon leek pasta": ["fusilli", "bacon", "leeks", "heavy cream", "grated parmesan"]},
    {"one pot chicken": ["chicken breasts", "red pepper", "chicken broth", "rice", "cream of chicken soup", "broccoli",
                         "shredded cheddar"]},
    {"grilled cheese": ["bread", "butter", "american cheese"]},
    {"breakfast for dinner": ["eggs", "bacon", "pancake mix", "syrup"]},
    {"tacos": ["ground beef", "taco seasoning", "taco shells", "shredded cheddar", "sour cream", "lettuce", "queso"]},
    {"spaghetti": ["spaghetti", "tomato sauce", "ground beef", "garlic bread", "parmesan cheese"]},
    {"hot dogs": ["hot dogs", "hot dog buns", "broccoli", "cheesy shells", "chips"]},
    {"chicken pot pie": ["chicken breasts", "frozen mixed veggies", "cream of chicken soup", "pie crust", "milk",
                         "chicken broth"]},
    {"chili": ["ground beef", "onion", "salsa", "kidney beans", "chili powder", "tomato soup"]},
]

categories = [
    {"produce": ["leeks", "red pepper", "broccoli", "lettuce", "onion"]},
    {"deli": ["american cheese"]},
    {"snack": ["chips", "salsa", "queso"]},
    {"breakfast": ["eggs", "pancake mix", "syrup"]},
    {"canned goods": ["loaded potato soup", "cream of chicken soup", "tomato soup"]},
    {"spices": ["yeast", "taco seasoning", "chili powder"]},
    {"pasta": ["fusilli", "spaghetti", "pizza sauce", "tomato sauce"]},
    {"meat": ["pepperoni", "ham", "bacon", "chicken breasts", "ground beef", "hot dogs"]},
    {"breads": ["grands rolls", "bread", "taco shells", "pie crust", "hot dog buns"]},
    {"dairy": ["milk", "shredded mozzarella", "smoked gouda", "grated parmesan", "shredded cheddar",
               "sour cream", "heavy cream", "butter", "eggs"]},
    {"frozen": ["frozen peas", "frozen mixed veggies"]},
]


# Generate a list of meals by randomly selecting them from the list above
# try to avoid duplicate meals within the same time frame
# print all the meal names in a readable format
# then print all the ingredients for all selected meals into a separate grocery list
# the lists are printed in a readable format
# each ingredient will have a quantity next to it
# duplicate items should increase the quantity
def generate(days=7):
    import random
    import collections
    # create a list to store the meals
    meal_list = []
    # create a list to store the ingredients
    grocery_list = []
    # create a counter to store the quantity of each ingredient
    grocery_counter = collections.Counter()
    # loop through the number of days
    for i in range(days):
        # randomly select a meal
        meal = random.choice(meals)
        while meal in meal_list and len(meal_list) > 0:
            meal = random.choice(meals)
        # check if the meal is already in the list
        if meal not in meal_list:
            # add the meal to the list
            meal_list.append(meal)
            # loop through the ingredients of the meal
            for ingredient in meal.values():
                # loop through the ingredients
                for item in ingredient:
                    # add the ingredient to the grocery list
                    grocery_list.append(item)
                    # increment the quantity of the ingredient
                    grocery_counter[item] += 1
    # print the meals
    print()
    print("Meals:\n")
    for meal in meal_list:
        print(list(meal.keys())[0])
    print()
    print("-----------------------\n")
    # print the grocery list by category
    print("Grocery List:\n")
    for category in categories:
        for key, value in category.items():
            print(f"{key.upper()}:")
            for item in value:
                if item in grocery_counter:
                    print(f"{item} ({grocery_counter[item]})")
            print()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # call generate but use user input to get the number of days to generate
    generate(int(input("How many days of meals would you like to generate?")))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

