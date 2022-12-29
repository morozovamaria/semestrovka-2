import socket
import threading

from PyQt6.QtWidgets import QMainWindow, QApplication

import gamer1_ui
import gamer2_ui
import main_ui_1
import main_ui_2

from functools import partial


class Main1(QMainWindow, main_ui_1.Ui_Main_1):
    def __init__(self):
        super(Main1, self).__init__()
        self.setupUi(self)
        self.gamer_1 = None

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(('127.0.0.1', 9000))

        self.play_button_1.clicked.connect(self.open_gamer_1)

    def open_gamer_1(self):
        self.close()
        self.gamer_1 = Gamer1()
        self.gamer_1.show()


class Main2(QMainWindow, main_ui_2.Ui_Main_2):
    def __init__(self):
        super(Main2, self).__init__()
        self.setupUi(self)
        self.gamer_2 = None

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(('127.0.0.1', 9000))

        self.play_button_2.clicked.connect(self.open_gamer_2)

    def open_gamer_2(self):
        self.close()
        self.gamer_2 = Gamer2()
        self.gamer_2.show()


class Gamer1(QMainWindow, gamer1_ui.Ui_Gamer1):
    def __init__(self):
        super(Gamer1, self).__init__()
        self.setupUi(self)
        # self.other_window = Gamer2()

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(('127.0.0.1', 9000))

        self.send.clicked.connect(self.write)

    def write(self):
        word = self.input_word.text()
        # self.other_window.word.append(word)
        self.input_word.setText('')
        self.client.send(word.encode('ascii'))


class Gamer2(QMainWindow, gamer2_ui.Ui_Gamer2):
    def __init__(self):
        super(Gamer2, self).__init__()
        self.labels = None
        self.setupUi(self)

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(('127.0.0.1', 9000))

    #     self.buttons = self.buttons_generate(self)
    #     for i in range(26):
    #         self.buttons[i].clicked.connect(partial(self.test, i))
    #
    # def test(self, index):
    #     self.label.setText(f"{chr(index+65)}")

    @staticmethod
    def buttons_generate(cls):
        buttons = []
        for i in range(26):
            buttons.append(getattr(cls, f"pushButton_{i+1}"))
        return buttons


if __name__ == "__main__":
    app = QApplication([])
    window_1 = Main1()
    window_2 = Main2()
    window_2.show()
    window_1.show()
    app.exec()



