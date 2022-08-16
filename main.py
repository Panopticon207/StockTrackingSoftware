import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from girisekrani import *
from Anapencere import *
from login import loginpage
import sqlite3
from kartolusturma import Kartolusturpage

app = QApplication([])
pencere = loginpage()
pencere.show()
app.exec()









