# Module Imports
import mariadb
import sys

class DatabaseConnection:
    def __init__(self, username:str, password:str, host:str, port:int, database:str):
        self.username = username
        self.password = password
        self.host = host
        self.port = port
        self.database = database
        self.good = True
        
        try:
            self.connection = mariadb.connect(
                user=self.username,
                password=self.password,
                host=self.host,
                port=self.port,
                database=self.database
            )

            self.cursor = self.connection.cursor()
        except mariadb.Error as e:
            self.good = False
            self.error = e
            
    def available(self):
        if not self.good:
            print(f"Error connecting to MariaDB Platform: {self.error}")
            return False
        else:
            return True

    def commit(self):
        self.connection.commit()

    def rollback(self):
        self.connection.rollback()