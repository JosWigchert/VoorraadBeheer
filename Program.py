import DatabaseConnection

import os
from dotenv import load_dotenv

load_dotenv()

database = DatabaseConnection.DatabaseConnection(
    os.getenv('USERNAME'), 
    os.getenv('PASSWORD'), 
    os.getenv('HOST'), 
    int(os.getenv('PORT')),
    os.getenv('DATABASE')
)

print(database.get_products())