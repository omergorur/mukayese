# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication , QWidget, QLabel, QPlainTextEdit, QPushButton, QGridLayout, QMainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

class MainGrid(QWidget):
    def __init__(self):
        super().__init__()
        self.initGrid()
        self.setStyleSheet('font-size: 17px')
    def initGrid(self):
        self.lb1 = QLabel('Listem')
        self.lb2 = QLabel('Liste')
        self.lb3 = QLabel('Sonuç')
        self.lb1.setAlignment(Qt.AlignHCenter)
        self.lb2.setAlignment(Qt.AlignHCenter)
        self.lb3.setAlignment(Qt.AlignHCenter)


        self.in1 = QPlainTextEdit()
        self.in1.setObjectName("aranan")
        self.in1.setPlaceholderText("Aranacak Satırlar")

        self.in2 = QPlainTextEdit()
        self.in2.setObjectName("arayan")
        self.in2.setPlaceholderText("Arayan Satırlar")

        self.in3 = QPlainTextEdit()
        self.in3.setObjectName("sonuc")
        self.in3.setReadOnly(True)



        self.bt1 = QPushButton()
        self.bt1.setObjectName("aynıları")
        self.bt1.setText("Olanları Bul")
        self.bt1.clicked.connect(self.bt1_click)

        self.bt2 = QPushButton()
        self.bt2.setObjectName("farklılar")
        self.bt2.setText("Olmayanları Bul")
        self.bt2.clicked.connect(self.bt2_click)

        self.bt3 = QPushButton()
        self.bt3.setObjectName("temizle")
        self.bt3.setText("Temizle")
        self.bt3.clicked.connect(self.bt3_click)

        layout = QGridLayout()
        layout.addWidget(self.lb1, 0,0)
        layout.addWidget(self.lb2, 0, 1)
        layout.addWidget(self.in1, 1, 0)
        layout.addWidget(self.in2, 1, 1)
        layout.addWidget(self.lb3, 2, 0, 1, 0)
        layout.addWidget(self.in3, 3, 0, 1, 0)
        layout.addWidget(self.bt1, 4, 0)
        layout.addWidget(self.bt2, 4, 1)
        layout.addWidget(self.bt3, 5, 0, 1, 0)

        self.setLayout(layout)

    def bt1_click(self):
        arananlar = self.in1.toPlainText().split("\n")
        arayanlar = self.in2.toPlainText().split("\n")
        aynilar = [oge for oge in arayanlar if oge in arananlar]
        self.lb3.setText("Listemde olan satırlar")
        self.lb3.setAlignment(Qt.AlignHCenter)
        self.in3.setPlainText("\n".join(aynilar))

    def bt2_click(self):
        arananlar = self.in1.toPlainText().split("\n")
        arayanlar = self.in2.toPlainText().split("\n")
        farkli = [oge for oge in arayanlar if oge not in arananlar]
        self.lb3.setText("Listemde olmayan satırlar")
        self.lb3.setAlignment(Qt.AlignHCenter)
        self.in3.setPlainText("\n".join(farkli))

    def bt3_click(self):
        self.in1.setPlainText("")
        self.in2.setPlainText("")
        self.in3.setPlainText("")
        self.lb3.setText("Sonuç")
        self.lb3.setAlignment(Qt.AlignHCenter)


class MainWin(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

        self.setGeometry(50, 50, 600, 500)
        self.setWindowTitle("Mukayase v1.0")
        self.setWindowIcon(QIcon("bulut-klinik-logo.png"))

    def initUI(self):
        centralGrid = MainGrid()
        centralGrid.sizeHint()
        self.setCentralWidget(centralGrid)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    gui = MainWin()
    sys.exit(app.exec_())