# Form implementation generated from reading ui file '.\ui\main.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(334, 298)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setStyleSheet("font: 11pt \"Segoe UI\";")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit_en = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_en.setStyleSheet("border-color: rgb(131, 131, 131);")
        self.lineEdit_en.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.lineEdit_en.setObjectName("lineEdit_en")
        self.verticalLayout.addWidget(self.lineEdit_en)
        self.lineEdit_vi = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_vi.setObjectName("lineEdit_vi")
        self.verticalLayout.addWidget(self.lineEdit_vi)
        self.btn_audio = QtWidgets.QPushButton(self.tab)
        self.btn_audio.setObjectName("btn_audio")
        self.verticalLayout.addWidget(self.btn_audio)
        self.btn_add = QtWidgets.QPushButton(self.tab)
        self.btn_add.setObjectName("btn_add")
        self.verticalLayout.addWidget(self.btn_add)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_en = QtWidgets.QLabel(self.tab_2)
        self.label_en.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        self.label_en.setFont(font)
        self.label_en.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_en.setStyleSheet("font: 700 12pt \"Segoe UI\";")
        self.label_en.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_en.setObjectName("label_en")
        self.verticalLayout_3.addWidget(self.label_en)
        self.rb_1 = QtWidgets.QRadioButton(self.tab_2)
        self.rb_1.setObjectName("rb_1")
        self.buttonGroup = QtWidgets.QButtonGroup(mainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.rb_1)
        self.verticalLayout_3.addWidget(self.rb_1)
        self.rb_2 = QtWidgets.QRadioButton(self.tab_2)
        self.rb_2.setObjectName("rb_2")
        self.buttonGroup.addButton(self.rb_2)
        self.verticalLayout_3.addWidget(self.rb_2)
        self.rb_3 = QtWidgets.QRadioButton(self.tab_2)
        self.rb_3.setObjectName("rb_3")
        self.buttonGroup.addButton(self.rb_3)
        self.verticalLayout_3.addWidget(self.rb_3)
        self.rb_4 = QtWidgets.QRadioButton(self.tab_2)
        self.rb_4.setObjectName("rb_4")
        self.buttonGroup.addButton(self.rb_4)
        self.verticalLayout_3.addWidget(self.rb_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_play = QtWidgets.QPushButton(self.tab_2)
        self.btn_play.setObjectName("btn_play")
        self.horizontalLayout.addWidget(self.btn_play)
        self.btn_check = QtWidgets.QPushButton(self.tab_2)
        self.btn_check.setObjectName("btn_check")
        self.horizontalLayout.addWidget(self.btn_check)
        self.btn_next = QtWidgets.QPushButton(self.tab_2)
        self.btn_next.setObjectName("btn_next")
        self.horizontalLayout.addWidget(self.btn_next)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.listWidget = QtWidgets.QListWidget(self.tab_3)
        self.listWidget.setGeometry(QtCore.QRect(0, 10, 256, 192))
        self.listWidget.setObjectName("listWidget")
        self.tabWidget.addTab(self.tab_3, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 334, 22))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "WordNote"))
        self.lineEdit_en.setPlaceholderText(_translate("mainWindow", "English"))
        self.lineEdit_vi.setPlaceholderText(_translate("mainWindow", "Tiếng Việt"))
        self.btn_audio.setText(_translate("mainWindow", "Audio"))
        self.btn_add.setText(_translate("mainWindow", "Add"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("mainWindow", "Add New"))
        self.label_en.setText(_translate("mainWindow", "TextLabel"))
        self.rb_1.setText(_translate("mainWindow", "RadioButton"))
        self.rb_2.setText(_translate("mainWindow", "RadioButton"))
        self.rb_3.setText(_translate("mainWindow", "RadioButton"))
        self.rb_4.setText(_translate("mainWindow", "RadioButton"))
        self.btn_play.setText(_translate("mainWindow", "Audio"))
        self.btn_check.setText(_translate("mainWindow", "Check"))
        self.btn_next.setText(_translate("mainWindow", "Next"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("mainWindow", "Practise"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("mainWindow", "List"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec())
