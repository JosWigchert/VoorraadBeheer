from .DatabaseConnection import DatabaseConnection

class Repository:
    def __init__(self, db: DatabaseConnection) -> None:
        self.db = db
        self.createCursor()

    def createCursor(self):
        self.cursor = self.db.connection.cursor(buffered=True)

    
    def available(self):
        return self.db.available()

    def commit(self):
        self.cursor.close()
        ret = self.db.commit()
        self.createCursor()
        return ret

    def rollback(self):
        self.cursor.close()
        ret = self.db.rollback()
        self.createCursor()
        return ret