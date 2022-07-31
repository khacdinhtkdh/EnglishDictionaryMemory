import random
import sys
import sqlite3
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMainWindow, QFileDialog, QRadioButton
from playsound import playsound
from mainui import Ui_MainWindow
import pygame.mixer as mixer
mixer.init()

DB_CREATE_TB = '''CREATE TABLE {} {}'''
DB_INSERT = ""
TABLE_NAME = 'dic'

class DBQSqllite():
    def __init__(self):
        self.con = sqlite3.connect('dictionary.db')
        self.cur = self.con.cursor()

        self.create_table()

    def create_table(self):
        # check if table exists
        listOfTables = self.cur.execute(
            """SELECT name FROM sqlite_master WHERE type='table'
            AND name='dic'; """).fetchall()
        if listOfTables == []:
            print('Table not found!')
            val = '(en text, vi text, audio BLOB)'
            self.cur.execute(DB_CREATE_TB.format('dic', val))
        else:
            print('Table found!')

    def insert(self, val):
        sqlite_query = "INSERT INTO dic (en, vi, audio) VALUES (?, ?, ?)"
        self.cur.execute(sqlite_query, val)
        self.con.commit()

    def getDatabase(self):
        self.cur.execute(f'SELECT * from {TABLE_NAME}')
        res = self.cur.fetchall()
        self.con.commit()
        return res

class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.audio_text = None
        self.id = 0
        self.vi = ""

        self.btn_audio.clicked.connect(self.get_audio_file)
        self.btn_add.clicked.connect(self.add_dictionary)
        self.btn_next.clicked.connect(self.random_id)
        self.btn_check.clicked.connect(self.check_answer)
        self.btn_play.clicked.connect(self.play_audio)
        self.tabWidget.currentChanged.connect(self.on_tab_change)

        self.db = DBQSqllite()
        self.data = self.db.getDatabase()
        self.random_id()

        self.list_rb = [self.rb_1, self.rb_2, self.rb_3, self.rb_4]

    def show_list(self):
        for word in self.data:
            self.listWidget.addItem(word[0])

    def on_tab_change(self, i):
        if i == 1:
            self.data = self.db.getDatabase()
            self.random_id()
        if i == 2:
            self.show_list()

    def reset_rb(self):
        for srb in self.buttonGroup.buttons():
            srb.setStyleSheet('color:black')

    def random_id(self):
        self.reset_rb()
        if len(self.data) == 0:
            return
        self.id = random.randrange(0, len(self.data))
        en = self.data[self.id][0]
        self.vi = self.data[self.id][1]
        self.write_audio_file(self.data[self.id][2])

        self.label_en.setText(en)

        rb = [self.vi]

        for i in range(3):
            id = random.randrange(0, len(self.data))
            rb.append(self.data[id][1])

        for srb in self.buttonGroup.buttons():
            text = str(random.choice(rb))
            srb.setText(text)
            rb.remove(srb.text())

    def check_answer(self):
        # id = self.find_checked_radiobutton(self.buttonGroup)
        # print(id)
        print(self.buttonGroup.checkedButton().text())
        for srb in self.buttonGroup.buttons():
            if srb.isChecked() and srb.text() == self.vi:
                srb.setStyleSheet("color:green")
            elif srb.isChecked():
                srb.setStyleSheet("color:red")

    def find_checked_radiobutton(self, radiobuttons):
        for items in radiobuttons:
            if items.isChecked():
                checked_radiobutton = items.text()
                return checked_radiobutton

    def play_audio(self):
        mixer.music.load('temp.mp3')
        mixer.music.play()

    def write_audio_file(self, data):
        mixer.music.unload()
        with open('temp.mp3', 'wb+') as file:
            file.write(data)
            file.close()

    def get_audio_file(self):
        path = QFileDialog.getOpenFileName(self, "", "", '*.mp3')
        if path[0]:
            with open(path[0], 'rb') as file:
                self.audio_text = file.read()
                file.close()

    def add_dictionary(self):
        en = self.lineEdit_en.text()
        vi = self.lineEdit_vi.text()
        val = (en, vi, self.audio_text)
        print(en, vi)
        self.db.insert(val)


class ErrorApp:
    # ...

    def raise_error(self):
        assert False

def excepthook(exc_type, exc_value, exc_tb):
    import traceback
    tb = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
    print("error message:\n", tb)
    QtWidgets.QApplication.quit()

sys.excepthook = excepthook
e = ErrorApp()
app = QtWidgets.QApplication(sys.argv)
MainWindow = Main()
sys.exit(app.exec())
