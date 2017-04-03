#!/usr/bin/env python
#-*-coding:utf-8-*-

import sys

from PyQt5.QtWidgets import (QApplication, QLineEdit, QMainWindow, QPushButton,
                             QRadioButton)


class Application(QMainWindow):
    def __init__(self):
        super(Application, self).__init__()
        self.title = "qwe加密"
        self.width = 220
        self.height = 90
        self.left = 500
        self.top = 300
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.button = QPushButton('calc', self)
        self.button.move(140, 60)
        self.button.resize(70, 20)
        self.button.clicked.connect(self.click)

        self.textbox = QLineEdit(self)
        self.textbox.move(10, 10)
        self.textbox.resize(200, 20)
        self.textbox.setPlaceholderText("明文")

        self.resultTextbox = QLineEdit(self)
        self.resultTextbox.move(10, 35)
        self.resultTextbox.resize(200, 20)
        self.resultTextbox.setPlaceholderText("结果")

        self.show()

    def click(self):
        cipherText = self.textbox.text()
        if cipherText != "":
            z = ""
            for k in cipherText:
                n = 0
                for i in "qwertyuiopasdfghjklzxcvbnm":
                    n = n + 1
                    if i == k:
                        z = z + (chr(n + 96))
            self.resultTextbox.setText(z)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Application()
    sys.exit(app.exec_())
