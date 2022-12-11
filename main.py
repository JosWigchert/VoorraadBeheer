from Database.DatabaseConnection import DatabaseConnection
from Database.IngredientRepository import IngredientRepository
from Database.ProductRepository import ProductRepository

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

ingredientsRepo = IngredientRepository(database)
productRepo = ProductRepository(database)


print(f"Is database available: {database.available()}")
print("1:", ingredientsRepo.getIngredients())
print("2:", ingredientsRepo.ingredientExists("Boter"))
print("3:", ingredientsRepo.ingredientExists("Bloem"))
print("4:", ingredientsRepo.getIngredient("Boter"))
print("5:", ingredientsRepo.getIngredient("Bloem"))
print("6:", ingredientsRepo.addIngredient("Bloem", 2, 1))
print("7:", ingredientsRepo.getIngredient("Bloem"))
print("8:", ingredientsRepo.updateIngredientAmountAdd("Boter", -25.5))
print("9:", ingredientsRepo.ingredientExists("Bloem"))
print("10:", ingredientsRepo.getIngredient("Bloem"))
print("11:", ingredientsRepo.getIngredient("Boter"))
print("12:", ingredientsRepo.updateIngredientAmountAdd("Boter", 50))
print("13:", ingredientsRepo.getIngredient("Boter"))
print("14:", ingredientsRepo.removeIngredient("Bloem"))
print("15:", ingredientsRepo.commit())

print("1:", productRepo.getProducts())
print("2:", productRepo.addProduct("TestProduct1", 100))
print("3:", productRepo.productExists("testProduct1"))
print("4:", productRepo.productExists("TestProduct2"))
print("5:", productRepo.getProduct("testProduct1"))
print("6:", productRepo.getProduct("TestProduct2"))
print("7:", productRepo.addProduct("TestProduct2", 2))
print("8:", productRepo.getProduct("TestProduct2"))
print("9:", productRepo.updateProductAmountAdd("testProduct1", -25))
print("10:", productRepo.productExists("TestProduct2"))
print("11:", productRepo.getProduct("TestProduct2"))
print("12:", productRepo.getProduct("testProduct1"))
print("13:", productRepo.updateProductAmountAdd("testProduct1", 50))
print("14:", productRepo.getProduct("testProduct1"))
print("15:", productRepo.removeProduct("TestProduct2"))
print("15:", productRepo.removeProduct("TestProduct1"))
print("16:", productRepo.productExists("TestProduct2"))
print("17:", productRepo.rollback())

