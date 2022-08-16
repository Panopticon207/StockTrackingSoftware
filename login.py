from  PyQt5.QtWidgets import *
from girisekrani import Ui_GirisEkran
from apencere import AnapencerePage



class loginpage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.loginform = Ui_GirisEkran ()
        self.loginform.setupUi(self)
        self.loginform.girisbuton.clicked.connect(self.Girisyap)
        self.anapencereac = AnapencerePage()
        self.anapencereac.show()



    def Girisyap (self):
        kadi= self.loginform.lineEdit_kullaniciadi.text()
        sifre = self.loginform.lineEdit_sifre.text()
        if kadi == "furkan" and sifre == "123":
            self.hide()
            self.anapencereac.show()



