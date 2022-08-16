from  PyQt5.QtWidgets import *
from stokhareket import Ui_StokHareket
import json
from apencere import *


class shareketform (QMainWindow):
    def __init__(self, apencere) -> None:
        super().__init__()
        self.apencere = apencere
        self.shareket = Ui_StokHareket()
        self.shareket.setupUi(self)
        self.shareket.pushButton_HareketAra.clicked.connect(self.IDARA)
        self.shareket.pushButton_HareketAra.clicked.connect(self.baskaara)
        self.shareket.pushButton_sil.clicked.connect(self.kayit_sil)

    def IDARA (self):
        y = self.shareket.lineEdit_hareketara.text()
        f = open("veriler.json", "r")
        n = 0
        t = -1
        Kartlar = json.load(f)
        self.shareket.tableWidget_ust.clear()
        self.shareket.tableWidget_ust.setHorizontalHeaderLabels(("ID","Stok Adı","Marka","Model","Miktar","Açıklama"))
        try:
            for a, b in enumerate(Kartlar["Kartlar"]):
                for c, d in enumerate(b.items()):
                    n = 0
                    try:
                        if int(y) in d:
                            t = t + 1
                            for i in b:
                                if n > 5:
                                    break
                                self.shareket.tableWidget_ust.setItem(t, n, QTableWidgetItem(str(b[i])))
                                n = n + 1
                    except:
                        if str(y) in d:
                            t = t + 1
                            for i in b:
                                if n > 5:
                                    break
                                self.shareket.tableWidget_ust.setItem(t, n, QTableWidgetItem(str(b[i])))
                                n = n + 1
        except:pass
    def baskaara (self):
            self.shareket.tableWidget_alt.clear()
            self.shareket.tableWidget_alt.setHorizontalHeaderLabels(("Fatura No", "Fatura Tarih", "Satıcı", "Alıcı", "Miktar", "Açıklama"))
            y = self.shareket.lineEdit_hareketara.text()
            f = open("veriler.json", "r")
            x = 0
            t = -1
            Kartlar = json.load(f)
            try:
                for a, b in enumerate(Kartlar["Kartlar"]):
                    for c, d in enumerate(b.items()):
                        r = b["Hareketler"]
                        if int(y) in d:
                            for p in r:
                                t = t + 1
                                x = 0
                                for i,k in reversed(list(p.items())):
                                    self.shareket.tableWidget_alt.setItem(t, x, QTableWidgetItem(str(k)))
                                    x = x + 1
            except:pass

    def stokguncelle (self):
            XT =self.shareket.tableWidget_alt.currentRow()
            xx = 0
            t = -1
            f = open("veriler.json", "r")
            Kartlar = json.load(f)
            for a in (Kartlar["Kartlar"]):
                for b in (a.items()):
                    r = a["Hareketler"]
                    for p in r:
                        t = t + 1
                        for i, z in reversed(list(p.items())):
                            if t != XT:
                                continue
                            xx = xx + 1
                            if xx > 4:
                                if int(z) > 0:
                                    a["Miktar"] += -int(z)
                                    print(z)
                                if int(z) < 0:
                                    a["Miktar"] += int(-z)
            with open("veriler.json", "w") as out_file:
                json.dump(Kartlar, out_file, indent=6)
                out_file.close()

    def kayit_sil(self):

        XT =self.shareket.tableWidget_alt.currentRow()
        t = -1
        x = 0
        xx=0
        sil_mesaj = QMessageBox.question(self, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz ?",QMessageBox.Yes | QMessageBox.No)
        if sil_mesaj == QMessageBox.Yes:
            self.stokguncelle()
            try:
                f = open("veriler.json", "r")
                Kartlar = json.load(f)
                for a in (Kartlar["Kartlar"]):
                    for b in (a.items()):
                        r = a["Hareketler"]
                        if int(123) in b:
                            for p in r:
                                t = t + 1
                                x = 0
                                for i, z in reversed(list(p.items())):
                                    if t != XT:
                                        continue
                                    a["Hareketler"].remove(r[t])
                                    break
                shareketform.statusBar(self).showMessage("Kayıt Başarıyla Silindi", 1000)
                with open("veriler.json", "w") as out_file:
                    json.dump(Kartlar, out_file, indent=6)
                    out_file.close()
                self.IDARA()
                self.baskaara()
                self.apencere.kayit_listele()


            except:
                pass

        if sil_mesaj == QMessageBox.No:
            self.IDARA()
            self.baskaara()

