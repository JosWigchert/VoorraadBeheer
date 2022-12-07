# Module Imports
import mariadb
import sys

class DatabaseConnection:
    def __init__(self, username, password, host, port, database):
        self.username = username
        self.password = password
        self.host = host
        self.port = port
        self.database = database
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
            
            sys.exit(1)

    def available(self):
        if not self.good:
            print(f"Error connecting to MariaDB Platform: {self.error}")
            return False
        else:
            return True

    def get_products(self):
        if not self.available():
            return -1

        self.cursor.execute("CALL `GetProducts`()")

        results = []
        for item in self.cursor:
            results.append({"Id": item[0], "Product": item[1], "Amount": item[2], "Unit": item[3], "UnitSmall": item[4]})

        return results



