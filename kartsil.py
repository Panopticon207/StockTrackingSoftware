from  PyQt5.QtWidgets import *
from kayitsil import Ui_Kayitsil

class kayitsilme (QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.kayitsil = Ui_Kayitsil()
        self.kayitsil.setupUi(self)