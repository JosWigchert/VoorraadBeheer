from Database import DatabaseConnection, IngredientsRepository

from PyQt6.QtWidgets import QApplication, QLabel, QWidget
import PyQt6
from dotenv import load_dotenv
import os, sys

load_dotenv()

class Program:
    def __init__(self) -> None:
        self.database = DatabaseConnection.DatabaseConnection(
            os.getenv('DBUSER'), 
            os.getenv('PASSWORD'), 
            os.getenv('HOST'), 
            int(os.getenv('PORT')),
            os.getenv('DATABASE')
        )
        self.app = QApplication([])
        self.app.setWindowIcon(PyQt6.QtGui.QIcon('icon.png'))
        self.createWindow()
        
        self.window.show()
        sys.exit(self.app.exec())

    def createWindow(self):
        self.window = QWidget()
        self.window.setWindowTitle("Voorraad Beheer")
        self.window.setWindowIcon(PyQt6.QtGui.QIcon('icon.png'))
        self.window.setGeometry(100, 100, 280, 80)
        helloMsg = QLabel("<h1>Hello, World!</h1>", parent=self.window)
        helloMsg.move(60, 15)


program = Program()

