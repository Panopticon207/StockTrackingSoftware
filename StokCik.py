from  PyQt5.QtWidgets import *
from stokcikis import Ui_StokCikis
import json

class stokcikisform (QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.stokcik = Ui_StokCikis()
        self.stokcik.setupUi(self)
        self.stokcik.pushButton_StokCikis_CikisYap.clicked.connect(self.stokcikis)

    def stokcikis (self):
        f = open("veriler.json", "r")
        Kartlar = json.load(f)
        adet = self.stokcik.lineEdit_StokCikis_Adet.text()
        try:
            adet = int(adet)
            adet =int(-adet)
        except:pass
        alici = self.stokcik.lineEdit_Stok_Cikis_Alici.text()
        fatura_tarih = self.stokcik.lineEdit_StokCikis_FaturTarih.text()
        fatura_no = self.stokcik.lineEdit_StokCikis_FaturaNumara.text()


        z = self.stokcik.lineEdit_StokCikis_Adet.text()
        try:
            z =-int(z)
        except: pass
        y = self.stokcik.lineEdit_StokCikis_ID.text()
        try:
            for a, b in enumerate(Kartlar["Kartlar"]):
                for c, d in enumerate(b.items()):
                    if int(y) in d:
                        b["Miktar"] += z
                        b["Hareketler"].append({"Adet": adet,"Alici":alici, "Tedarikci": "Furkan Holding", "Fatura Tarih": fatura_tarih, "Fatura Numara": fatura_no})
                        stokcikisform.statusBar(self).showMessage("Stok çıkışı yapıldı", 1000)

            with open("veriler.json", "w") as out_file:
                json.dump(Kartlar, out_file, indent=6)
                out_file.close()

        except:
            pass