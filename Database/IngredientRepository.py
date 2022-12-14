from .DatabaseConnection import DatabaseConnection
from .Repository import Repository

class IngredientRepository(Repository):
    def __init__(self, db: DatabaseConnection) -> None:
        Repository.__init__(self, db)


    def ingredientExists(self, ingredient:str):
        if not self.available():
            return -1
        
        self.cursor.execute("CALL `IngredientExists`(%s)", [ingredient])

        return bool(self.cursor.fetchone()[0])
        

    def getIngredients(self):
        if not self.available():
            return -1

        self.cursor.callproc("GetIngredients")

        dbResult = self.cursor.fetchall()
        results = []
        for item in dbResult:
            results.append({"Id": item[0], "Ingredient": item[1], "Amount": item[2], "Unit": item[3], "UnitSmall": item[4]})

        return results

    def getIngredient(self, ingredient:str):
        if not self.available():
            return -1
        if not self.ingredientExists(ingredient):
            return -2

        self.cursor.execute("CALL `GetIngredient`(%s)", [ingredient])

        item = self.cursor.fetchone()
        return {"Id": item[0], "Ingredient": item[1], "Amount": item[2], "Unit": item[3], "UnitSmall": item[4]}

    def addIngredient(self, ingredient:str, amount:float, unitId:int):
        if not self.available():
            return -1

        self.cursor.execute("CALL `AddIngredient`(%s, %d, %d)", [ingredient, amount, unitId])
        return True

    def updateIngredientAmount(self, ingredient:str, amount:float):
        if not self.available():
            return -1
        if not self.ingredientExists(ingredient):
            return -2

        self.cursor.execute("CALL `updateIngredientAmount`(%s, %d)", [ingredient, amount])
        return True

    def updateIngredientAmountAdd(self, ingredient:str, amount:float):
        if not self.available():
            return -1
        if not self.ingredientExists(ingredient):
            return -2

        self.cursor.execute("CALL `updateIngredientAmountAdd`(%s, %d)", [ingredient, amount])
        return True

    def removeIngredient(self, ingredient:str):
        if not self.available():
            return -1
        if not self.ingredientExists(ingredient):
            return -2

        self.cursor.execute("CALL `RemoveIngredient`(%s)", [ingredient])
        return True