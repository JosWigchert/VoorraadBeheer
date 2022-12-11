from .DatabaseConnection import DatabaseConnection
from .Repository import Repository

class ProductRepository(Repository):
    def __init__(self, db: DatabaseConnection) -> None:
        Repository.__init__(self, db)


    def productExists(self, product:str):
        if not self.available():
            return -1
        
        self.cursor.execute("CALL `ProductExists`(%s)", [product])

        return bool(self.cursor.fetchone()[0])
        

    def getProducts(self):
        if not self.available():
            return -1

        self.cursor.execute("CALL `GetProducts`()")

        results = []
        for item in self.cursor:
            print()
            results.append({"Id": item[0], "Product": item[1], "Amount": item[2]})

        return results

    def getProduct(self, product:str):
        if not self.available():
            return -1
        if not self.productExists(product):
            return -2

        self.cursor.execute("CALL `GetProduct`(%s)", [product])

        item = self.cursor.fetchone()
        return {"Id": item[0], "Product": item[1], "Amount": item[2]}

    def addProduct(self, product:str, amount:float):
        if not self.available():
            return -1

        self.cursor.execute("CALL `AddProduct`(%s, %d)", [product, amount])
        return True

    def updateProductAmount(self, product:str, amount:float):
        if not self.available():
            return -1
        if not self.productExists(product):
            return -2

        self.cursor.execute("CALL `updateProductAmount`(%s, %d)", [product, amount])
        return True

    def updateProductAmountAdd(self, product:str, amount:float):
        if not self.available():
            return -1
        if not self.productExists(product):
            return -2

        self.cursor.execute("CALL `updateProductAmountAdd`(%s, %d)", [product, amount])
        return True

    def removeProduct(self, product:str):
        if not self.available():
            return -1
        if not self.productExists(product):
            return -2

        self.cursor.execute("CALL `RemoveProduct`(%s)", [product])
        return True