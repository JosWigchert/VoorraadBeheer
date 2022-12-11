from .DatabaseConnection import DatabaseConnection

class Repository:
    def __init__(self, db: DatabaseConnection) -> None:
        self.db = db
    
    def available(self):
        return self.db.available()

    def commit(self):
        return self.db.commit()

    def rollback(self):
        return self.db.rollback()