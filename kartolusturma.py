from plistlib import UID
from  PyQt5.QtWidgets import *
from kartolustur import Ui_KartOlustur
import sqlite3
import json


class Kartolusturpage (QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.kartolustur = Ui_KartOlustur()
        self.kartolustur.setupUi(self)
        self.kartolustur.buton_kartolustur.clicked.connect (self.veriekle)


    def veriekle (self):
        UID = int (self.kartolustur.lineEdit_ID.text())
        Stokad = self.kartolustur.lineEdit_Stokadi.text()
        Marka = self.kartolustur.lineEdit_Marka.text()
        Model = self.kartolustur.lineEdit_Model.text()


        try:
            f = open("veriler.json", "r")
            Kartlar = json.load(f)
        except:
            Kartlar = {}
        if Kartlar.get("Kartlar"):
            dict = (Kartlar["Kartlar"])
            if UID not in [entry["ID"] for entry in dict]:
                Kartlar["Kartlar"].append({"ID":UID,"Ad":Stokad,"Marka":Marka,"Model":Model,"Miktar":0,"Aciklama": 0, "Hareketler": []})
                Kartolusturpage.statusBar(self).showMessage("Başarıyla Eklendi",1000)

            else:
                Kartolusturpage.statusBar(self).showMessage("Aynı ID ile oluşturulmuş bir kart zaten mevcut", 1000)
                print("Zaten Mevcut")

        else:
            Kartlar = {"Kartlar": [{"ID":UID,"Ad":Stokad,"Marka":Marka,"Model":Model,"Miktar":0,"Aciklama": 0, "Hareketler": []}]}

        with open("veriler.json", "w") as out_file:
            json.dump(Kartlar, out_file, indent=6)
            out_file.close()


        self.kartolustur.lineEdit_ID.setText("")
        self.kartolustur.lineEdit_Model.setText("")
        self.kartolustur.lineEdit_Marka.setText("")
        self.kartolustur.lineEdit_Stokadi.setText("")














        














