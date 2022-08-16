from  PyQt5.QtWidgets import *
from Anapencere import Ui_Anapencere
from kartolusturma import Kartolusturpage
from stokgir import stokgirform
from StokCik import stokcikisform
from shareket import shareketform
from kartsil import kayitsilme
from login import*
import json



class AnapencerePage (QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.anapencereform = Ui_Anapencere()
        self.anapencereform.setupUi(self)
        self.kartolusturform = Kartolusturpage ()
        self.stokgir = stokgirform()
        self.stokcik = stokcikisform()
        self.shareket = shareketform (self)
        self.kayitsil = kayitsilme ()
        self.anapencereform.stokkartolusturinmenu.triggered.connect(self.StokKartOlusturForm)
        self.anapencereform.stokgirisinmenu.triggered.connect (self.Stokgir)
        self.anapencereform.stokcikisinmenu.triggered.connect (self.Stokcik)
        self.anapencereform.stokhareketleriinmenu.triggered.connect (self.stokhareket)
        self.anapencereform.stokkartsilinmenu.triggered.connect (self.ksil)
        self.anapencereform.hepsinilistelebuton.clicked.connect (self.kayit_listele)
        self.anapencereform.urun_ara.clicked.connect(self.IDARA)



    def kayit_listele(self):

        f = open("veriler.json", "r")
        Kartlar = json.load(f)

        self.anapencereform.tableWidget.setHorizontalHeaderLabels(())
        for indexsatir, kayitnumarasi in enumerate (Kartlar["Kartlar"]):
            for indexsutun, kayitsutun in enumerate (list(kayitnumarasi.items())[0:6]):
                y = self.anapencereform.tableWidget.setItem(indexsatir,indexsutun,QTableWidgetItem(str(kayitsutun[1])))

    def IDARA (self):
        y = self.anapencereform.lineEdit_urunara.text()
        f = open("veriler.json", "r")
        x = 0
        t = -1
        Kartlar = json.load(f)
        self.anapencereform.tableWidget.clear()
        self.anapencereform.tableWidget.setHorizontalHeaderLabels(("ID","Stok Adı","Marka","Model","Miktar","Açıklama"))

        for a, b in enumerate(Kartlar["Kartlar"]):
            for c, d in enumerate(b.items()):
                x = 0
                try:
                    if int(y) in d:
                        t = t + 1
                        for i in b:
                            if x > 5:
                                break
                            print (i)
                            self.anapencereform.tableWidget.setItem(t, x, QTableWidgetItem(str(b[i])))
                            x = x + 1
                except:
                    if str(y) in d:
                        t = t + 1
                        for i in b:
                            if x > 5:
                                break
                            print (i)
                            self.anapencereform.tableWidget.setItem(t, x, QTableWidgetItem(str(b[i])))
                            x = x + 1


    def StokKartOlusturForm (self):
        self.kartolusturform.show()
    def Stokgir (self):
        self.stokgir.show()
    def Stokcik (self):
        self.stokcik.show()
    def stokhareket (self):
        self.shareket.show()
    def ksil (self):
        self.kayitsil.show()











