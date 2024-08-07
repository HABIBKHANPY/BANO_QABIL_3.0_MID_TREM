import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('path/to/your/credentials.json', scope)
client = gspread.authorize(creds)

def load_recipes(sheet_name):
    sheet = client.open(sheet_name).sheet1
    recipes = {}
    data = sheet.get_all_records()
    for row in data:
        recipe_name = row['Recipe']
        ingredients = row['Ingredients'].split(', ')
        recipes[recipe_name] = ingredients
    return recipes

def suggest_recipes(recipes, available_ingredients):
    suggested_recipes = []
    for recipe, ingredients in recipes.items():
        if all(ingredient in available_ingredients for ingredient in ingredients):
            suggested_recipes.append(recipe)
    return suggested_recipes

def main():
    print("Welcome to the Recipe Finder!")

    recipes = load_recipes('Recipe spreadsheet')

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
