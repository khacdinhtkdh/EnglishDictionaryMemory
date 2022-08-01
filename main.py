import random
import sys
import sqlite3
from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtWidgets import QMainWindow, QFileDialog
from mainui import Ui_mainWindow
import pygame.mixer as mixer

mixer.init()

DB_CREATE_TB = '''CREATE TABLE {} {}'''
DB_INSERT = ""
TABLE_NAME = 'dic'


class DBQSqlite:
    def __init__(self):
        self.con = sqlite3.connect('dictionary.db')
        self.cur = self.con.cursor()

        self.create_table()

    def create_table(self):
        # check if table exists
        list_of_tables = self.cur.execute(
            """SELECT name FROM sqlite_master WHERE type='table'
            AND name='dic'; """).fetchall()
        if not list_of_tables:
            print('Table not found!')
            val = '(en text, vi text, audio BLOB)'
            self.cur.execute(DB_CREATE_TB.format('dic', val))
        else:
            print('Table found!')

    def insert(self, val):
        sqlite_query = "INSERT INTO dic (en, vi, audio) VALUES (?, ?, ?)"
        self.cur.execute(sqlite_query, val)
        self.con.commit()

    def get_database(self):
        self.cur.execute(f'SELECT * from {TABLE_NAME}')
        res = self.cur.fetchall()
        self.con.commit()
        return res


def play_audio():
    mixer.music.load('temp.mp3')
    mixer.music.play()


def find_checked_radiobutton(radiobuttons):
    for items in radiobuttons:
        if items.isChecked():
            checked_radiobutton = items.text()
            return checked_radiobutton


def write_audio_file(data):
    mixer.music.unload()
    with open('temp.mp3', 'wb+') as file:
        file.write(data)
        file.close()


class Main(QMainWindow, Ui_mainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.audio_text = None
        self.id = 0
        self.vi = ""
        self.list_random = list()
        self.btn_audio.clicked.connect(self.get_audio_file)
        self.btn_add.clicked.connect(self.add_dictionary)
        self.btn_next.clicked.connect(self.random_id)
        self.btn_check.clicked.connect(self.check_answer)
        self.btn_play.clicked.connect(play_audio)
        self.tabWidget.currentChanged.connect(self.on_tab_change)

        self.db = DBQSqlite()
        self.data = self.db.get_database()
        self.random_id()

        self.list_rb = [self.rb_1, self.rb_2, self.rb_3, self.rb_4]

    def show_list(self):
        self.data = self.db.get_database()
        self.listWidget.clear()
        for word in self.data:
            self.listWidget.addItem(word[0])

    def on_tab_change(self, i):
        if i == 1:
            self.data = self.db.get_database()
            self.random_id()
        if i == 2:
            self.show_list()

    def reset_rb(self):
        for srb in self.buttonGroup.buttons():
            srb.setStyleSheet('color:black')

    def make_list_random(self):
        self.data = self.db.get_database()
        for i in range(len(self.data)):
            for k in range(5):
                self.list_random.append(i)

    def random_id(self):
        self.reset_rb()
        if len(self.data) == 0:
            return
        if len(self.list_random) == 0:
            self.make_list_random()
        self.id = random.choice(self.list_random)
        self.list_random.remove(self.id)
        en = self.data[self.id][0]
        self.vi = self.data[self.id][1]
        write_audio_file(self.data[self.id][2])

        self.label_en.setText(en)

        rb = [self.vi]
        id_rb = [self.id]
        idx = self.id
        for i in range(3):
            while idx in id_rb:
                idx = random.randrange(0, len(self.data))
            rb.append(self.data[idx][1])
            id_rb.append(idx)

        for srb in self.buttonGroup.buttons():
            text = str(random.choice(rb))
            srb.setText(text)
            rb.remove(srb.text())

        play_audio()

    def check_answer(self):
        # id = self.find_checked_radiobutton(self.buttonGroup)
        # print(id)
        print(self.buttonGroup.checkedButton().text())
        for srb in self.buttonGroup.buttons():
            if srb.isChecked() and srb.text() == self.vi:
                srb.setStyleSheet("color:green")
            elif srb.isChecked():
                srb.setStyleSheet("color:red")

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


def raise_error():
    assert False


class ErrorApp:
    # ...

    pass


def except_hook(exc_type, exc_value, exc_tb):
    import traceback
    tb = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
    print("error message:\n", tb)
    QtWidgets.QApplication.quit()


def icon_from_base64(base64):
    pixmap = QtGui.QPixmap()
    pixmap.loadFromData(QtCore.QByteArray.fromBase64(base64))
    m_icon = QtGui.QIcon(pixmap)
    return m_icon


base_icon = b'iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAYAAADimHc4AAAABmJLR0QA/wD/AP+gvaeTAAADUklEQVR4nO3dTUgUYRzH8d' \
            b'+ztkpqppViQUQgKEWXgk4l1kEyoTYlLQiMSk/lrS6BBHrqKp2WCCSMwJcOekiijKgIeqGTLVtUFKZZse6uL9uu83QqMHLNfZ71rzu' \
            b'/z3XcZx/ny8w8u+MgQEREbqWkJ5CqqfpLejneJ6' \
            b'/3alr3kSedg9PiGEAYAwhjAGEMIGyN7QErR8brtPK0KegKR6mcdC0hpsuL0zTyfPsDE0lXW4/Ki41' \
            b'+RWsBaoLBgqgufKI1dgKAhlq9a9xlZCVATTBYENFFH5TWRTbGcxMr14BoovApd35qjANUjozXwYMdNibjRsYBtPK02ZiIW5mfgpSusD' \
            b'AP17IQwJNtYR6uZR5Aa642DfCTsDAGEMYAwhhAGAMIYwBhDCCMAYQxgDAGEMYAwqzfE/5fVRtypd56ReERIIwBhDGAMAYQxgDCGEAY' \
            b'AwhjAGEMIIwBhDGAMAYQxgDCGEAYAwhjAGEMIEzsjtjwj2mj17damoc0HgHCMj6AVgrPD1TjcvcALvbdw/DRBjhZWdLT+sP44YrFHm' \
            b'ROl75FHtSOe7Px+LAP/S2t+FRWPm9b6cf3qL3pR/XtLnhjsaTj1AUmkm43fVA74wLM5OXjfv1J3Dl7Ht9LtyQdY/23CRy6dQO1XX7kh' \
            b'0P//BkGWMDfAUKbinH3xGkMNrUgWlC4pLHWTkVxsLcbvuvXsHFsdN42BljA7wBj27Zj8NQ5DDU2IZ6TYzSmN/4T+wb74fN3YuvbAID0' \
            b'BxBbhpp6s3sv+psv4EVVNRyPnbVE3JuNB75GPDxyHHuGh3DM32ll3GRW7RGwUpgeARm/DF3pGEAYAwhjAGEMIIwBhDGAMAYQxgDCG' \
            b'EAYAwhjAGEMIIwBhDGAMLs3ZOY0QtEYvkRimJydQ9xxrA6fiawFiM8k8Gp0ErE5V9+fWTIrAeKzCTz7HILmvl8y82uAA7weDXPnp8' \
            b'g4QGRqFjMJnutTZRxgLJz8L8soOeNrQPOuzVEA+Rbmsiq1G77ewucAxbO/AfN/4AD9zsZE3Mo4gFIYsDERtzIOkJVwOgEVsTEZNz' \
            b'IOcKV03VetcQYArwUpsPJlXEdJbo/WqgFA2MZ4bmLt29COktyeRMIpU0C7Bl4CiNoam4iIiIiIiIgyxS96Wto1qujZAwAAAABJRU' \
            b'5ErkJggg== '

sys.excepthook = except_hook
e = ErrorApp()
app = QtWidgets.QApplication(sys.argv)
icon = icon_from_base64(base_icon)
app.setWindowIcon(icon)
MainWindow = Main()
sys.exit(app.exec())
