# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from proga_class import *
from chat_bot_class import InstagramBot
from data import username, password

#username = InstagramBot

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.handler)  # обработчик кнопки "Запустить"
        self.ui.pushButton_2.clicked.connect(self.stoper)  # обработчик кнопки "Стоп"



    def handler(self):
        my_bot = InstagramBot(username, password)
        my_bot.login()
        green = True
        while green:
            my_bot.check_inbox_direct()
            my_bot.auto_otvet()
            if not green:
                break

    def stoper(self):
        my_bot = None




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())