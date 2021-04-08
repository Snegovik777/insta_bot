# -*- coding: utf-8 -*-

# Это вариант программы C ПОТОКАМИ!!!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from proga_class import *
from chat_bot_class import InstagramBot
from data import username, password

#username = InstagramBot


class MyThread(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)
        self.running = False  # Флаг выполнения

    def run(self):
        my_bot = InstagramBot(username, password)
        my_bot.login()
        self.running = True
        while self.running:  # Проверяем значение флага
            my_bot.check_inbox_direct()
            my_bot.auto_otvet()


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.on_start)  # обработчик кнопки "Запустить"
        self.ui.pushButton_2.clicked.connect(self.on_stop)  # обработчик кнопки "Стоп"


    def on_start(self):
        print('Запускаем поток')
        self.ui.mythread1.start()  # Запускаем поток

    def on_stop(self):
        self.ui.mythread1.wait(1000)
        print('Останавливаем поток')
        self.ui.mythread1.running = False  # Изменяем флаг выполнения потока

    def on_change(self, s):
        self.ui.label.setText(s)

#    def handler(self):
#        my_bot = InstagramBot(username, password)
#        my_bot.login()
#        green = True
#        while green:
#            my_bot.check_inbox_direct()
#            my_bot.auto_otvet()
#            if not green:
#                break


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())