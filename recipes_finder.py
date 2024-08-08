import requests

SHEETY_ENDPOINT = "https://api.sheety.co/956b4793baba2022781857e25b24a923/recipes/sheet1"

def load_recipes():
    try:
        response = requests.get(url=SHEETY_ENDPOINT)
        response.raise_for_status()
        data = response.json()
        
        recipes_data = data['Recipes']
        
        recipes = {}
        for item in recipes_data:
            recipe_name = item['Recipe']
            ingredients = item['Ingredients'].split(', ')
            recipes[recipe_name] = ingredients
        
        return recipes
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return {}

def suggest_recipes(recipes, available_ingredients):
    suggested_recipes = []
    for recipe, ingredients in recipes.items():
        if all(ingredient in available_ingredients for ingredient in ingredients):
            suggested_recipes.append(recipe)
    return suggested_recipes

def main():
    print("Welcome to the Recipe Finder!")

    recipes = load_recipes()

    if not recipes:
        print("No recipes found or an error occurred.")
        return

    available_ingredients = input("Enter the ingredients you have, separated by commas: ").strip().lower().split(", ")

    suggested_recipes = suggest_recipes(recipes, available_ingredients)

    if suggested_recipes:
        print("You can make the following recipes with the ingredients you have:")
        for recipe in suggested_recipes:
            print(f"- {recipe}")
    else:
        print("Sorry, no recipes match the ingredients you have.")

if __name__ == "__main__":
    main()
