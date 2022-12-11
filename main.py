from Database.DatabaseConnection import DatabaseConnection
from Database.IngredientsRepository import IngredientsRepository

from dotenv import load_dotenv
import os, sys

load_dotenv()

print("StartingProgram...")

print(f"Connecting to database: {os.getenv('USERNAME')}")

database = DatabaseConnection(
    os.getenv('DBUSER'), 
    os.getenv('PASSWORD'), 
    os.getenv('HOST'), 
    int(os.getenv('PORT')),
    os.getenv('DATABASE')
)

ingredientsRepo = IngredientsRepository(database)

print(f"Is database available: {database.available()}")
print("1:", ingredientsRepo.getIngredients())
print("2:", ingredientsRepo.ingredientExists("Boter"))
print("3:", ingredientsRepo.ingredientExists("Bloem"))
print("4:", ingredientsRepo.getIngredient("Boter"))
print("5:", ingredientsRepo.getIngredient("Bloem"))
print("6:", ingredientsRepo.addIngredient("Bloem", 2, 1))
print("7:", ingredientsRepo.getIngredient("Bloem"))
print("8:", ingredientsRepo.updateIngredientAmountAdd("Boter", -25))
print("9:", ingredientsRepo.ingredientExists("Bloem"))
print("10:", ingredientsRepo.getIngredient("Bloem"))
print("11:", ingredientsRepo.getIngredient("Boter"))
print("12:", ingredientsRepo.updateIngredientAmountAdd("Boter", 50))
print("13:", ingredientsRepo.getIngredient("Boter"))
print("14:", ingredientsRepo.removeIngredient("Bloem"))
print("15:", ingredientsRepo.commit())

