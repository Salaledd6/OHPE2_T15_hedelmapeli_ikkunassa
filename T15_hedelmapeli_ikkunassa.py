import random
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton

class Hedelmapeli(QMainWindow):
    def __init__(self):
        super().__init__()

        self.kiekot = [['🍒','🍓','🍐','🍋','🍉'], ['🍒','🍓','🍐','🍋','🍉'], ['🍒','🍓','🍐','🍋','🍉']]
        self.tulos = []
        self.saldo = 10

        self.setWindowTitle("Hedelmäpeli")
        self.setGeometry(100,100,350,250)
        self.setMinimumWidth(250)

        self.alustaIkkuna()

    def alustaIkkuna(self):
        self.e1 = QLabel("$", self)
        self.e1.setGeometry(70,10,30,30)

        self.e2 = QLabel("$", self)
        self.e2.setGeometry(110,10,30,30)

        self.e3 = QLabel("$", self)
        self.e3.setGeometry(150,10,30,30)

        self.p1 = QPushButton("Pelaa", self)
        self.p1.setGeometry(65,50,100,30)
        self.p1.clicked.connect(self.suorita_peli) # metodin nimi ilman sulkuja lopussa

        self.e4 = QLabel(f"Saldo: {self.saldo}", self)
        self.e4.setGeometry(65,100,100,30)
    
    def suorita_peli(self):
        if self.saldo > 0:
            self.saldo -= 1
        
            self.tulos.clear()

            for alilista in self.kiekot:
                self.tulos.append(random.choice(alilista))

            self.e1.setText(self.tulos[0])
            self.e2.setText(self.tulos[1])
            self.e3.setText(self.tulos[2])

            if self.tulos[0] == self.tulos[1] == self.tulos[2]:
                self.saldo += 5

            self.e4.setText(f"Saldo: {self.saldo}")
        else:
            self.e4.setText("Rahat loppu")
    
def main():
    sovellus = QApplication(sys.argv) # olio luokasta QApplication
    ikkuna = Hedelmapeli() # olio luokasta Omaikkuna, joka peri QMainWindow ominaisuudet
    ikkuna.show() # kutsutaan ikkuna oliolle metodia show()
    sys.exit(sovellus.exec()) # käynnistetään sovellus(sovellus.exec()). Kun loppuu, välitetään paluuarvo sys.exit() metodille

if __name__ == "__main__":
    main()
