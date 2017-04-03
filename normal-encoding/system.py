#!/usr/bin/env python
#-*-coding:utf-8-*-
import sys

from PyQt5.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
                             QMenu, QPushButton, QRadioButton, QTextEdit,
                             QVBoxLayout)


class Application(QMainWindow):  # inhert from QMainWindow

    def __init__(self):
        super(Application, self).__init__()
        self.title = "test"  # set window title
        self.left = 100  # set window padding left your desktop
        self.top = 10  # set window padding letf your desktop
        self.width = 320  # set window width
        self.height = 200  # set window height
        self.initUI()  # init window

    def initUI(self):
        self.setWindowTitle(self.title)  # show window title
        self.setGeometry(self.left, self.top, self.width, self.height)  # set window

        self.label = QLabel("test label: ", self)  # add label
        self.label.move(10, 5)  # move label left and top

        self.textbox = QLineEdit(self)  # add textbox
        self.textbox.move(80, 10)  # move textbox left and top
        self.textbox.resize(100, 20)  # resize textbox width and height

        self.button = QPushButton('Show text', self)  # add button
        self.button.move(190, 10)  # move botton left and top
        self.button.resize(70, 20)  # resize button width and height
        self.button.clicked.connect(self.click)  # add click event

        self.anotherButton = QPushButton('Another button', self)
        self.anotherButton.move(190, 50)
        self.anotherButton.resize(100, 20)
        self.anotherButton.clicked.connect(self.click)

        self.radio = QRadioButton("aa", self)
        self.radio.move(10, 100)
        self.radioAnother = QRadioButton("bb", self)
        self.radioAnother.move(10, 120)

        self.mainLayout = QVBoxLayout()
        self.textEditor = QTextEdit()
        self.textEditor.setPlainText("aa")
        self.mainLayout.addWidget(self.textEditor)
        self.show()

    def click(self):
        self.textbox.setText("just test.")
        print("get textbox: ", self.textbox.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Application()
    sys.exit(app.exec_())
