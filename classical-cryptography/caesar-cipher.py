#!/usr/bin/env python
# -*-coding:utf-8-*-

import sys

from PyQt5.QtWidgets import (QApplication, QLineEdit, QMainWindow, QPushButton,
                             QRadioButton)


class Application(QMainWindow):
    def __init__(self):
        super(Application, self).__init__()
        self.title = "凯撒密码"
        self.width = 220
        self.height = 200
        self.left = 500
        self.top = 300
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.radio = QRadioButton("带字符", self)
        self.radio.move(10, 10)
        self.radio.setChecked(True)
        self.radioAnother = QRadioButton("不带字符", self)
        self.radioAnother.move(10, 30)

        self.button = QPushButton('calc', self)
        self.button.move(140, 10)
        self.button.resize(70, 20)
        self.button.clicked.connect(self.click)

        self.textbox = QLineEdit(self)
        self.textbox.move(10, 100)
        self.textbox.resize(200, 20)
        self.textbox.setPlaceholderText("密文")

        self.resultTextbox = QLineEdit(self)
        self.resultTextbox.move(10, 130)
        self.resultTextbox.resize(200, 20)
        self.resultTextbox.setPlaceholderText("结果")

        self.show()

    def click(self):
        if self.textbox.text() != "":
            if self.radio.isChecked():
                self.withCharacter(self.textbox.text())
            elif self.radioAnother.isChecked():
                self.withoutCharacter(self.textbox.text())

    def withCharacter(self, cipherText):
        for p in range(127):
            str1 = ''
            for char in cipherText:
                temp = chr((ord(char) + p) % 127)
                if 32 < ord(temp) < 127:
                    str1 = str1 + temp
                    feel = 1
                else:
                    feel = 0
                    break
            if feel == 1:
                self.resultTextbox.setText(str1)

    def withoutCharacter(self, cipherText):
        self.resultTextbox.setText("nothing")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Application()
    sys.exit(app.exec_())
