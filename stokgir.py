from  PyQt5.QtWidgets import *
from stokgiris import Ui_Form
import sqlite3
import json

class stokgirform (QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.stokgir = Ui_Form()
        self.stokgir.setupUi(self)
        self.stokgir.pushButton_GirisYap.clicked.connect(self.stokgiris)



    def stokgiris (self):
        f = open("veriler.json", "r")
        Kartlar = json.load(f)
        adet = self.stokgir.lineEdit_Stokgiris_Adet.text()
        tedarikci = self.stokgir.lineEdit_StokGiris_Tedarikci.text()
        fatura_tarih = self.stokgir.lineEdit_StokGiris_FaturaTarih.text()
        fatura_no = self.stokgir.lineEdit_StokGiris_FaturaNumara.text()


        z = self.stokgir.lineEdit_Stokgiris_Adet.text()
        y = self.stokgir.lineEdit_StokgirisID.text()
        try:
            for a, b in enumerate(Kartlar["Kartlar"]):
                for c, d in enumerate(b.items()):
                    if int(y) in d:
                        b["Miktar"] += int(z)
                        b["Hareketler"].append({"Adet": adet,"Alıcı":"Furkan Holding", "Tedarikci": tedarikci, "Fatura Tarih": fatura_tarih, "Fatura Numara": fatura_no})
                        stokgirform.statusBar(self).showMessage("Stok girişi yapıldı", 1000)

            with open("veriler.json", "w") as out_file:
                json.dump(Kartlar, out_file, indent=6)
                out_file.close()
        except:
            stokgirform.statusBar(self).showMessage("Stok Girişi Başarısız", 1000)


        self.stokgir.lineEdit_Stokgiris_Adet.setText("")
        self.stokgir.lineEdit_StokgirisID.setText("")
        self.stokgir.lineEdit_StokGiris_FaturaTarih.setText("")
        self.stokgir.lineEdit_StokGiris_FaturaNumara.setText("")
        self.stokgir.lineEdit_StokGiris_Tedarikci.setText("")
