# -*- coding: utf-8 -*-
# Converter UI to PY
# Create 15.07.2021
# Author edition script: Bezginov Igory
# This program is free software

"""
Python-3
Install  Modules PyQt5

"""

from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap
import subprocess
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = " Converter UI to PY"
        self.top = 100
        self.left = 100
        self.width = 900
        self.height = 270

        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("icon_star.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)

        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(10, 10, 881, 231))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")

        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(10, 20, 711, 20))
        self.lineEdit.setObjectName("lineEdit")

        self.open_Button = QtWidgets.QPushButton("Open UI File", self.frame)
        self.open_Button.setGeometry(QtCore.QRect(730, 20, 141, 23))
        self.open_Button.clicked.connect(self.open_file)

        self.lineEdit_py = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_py.setGeometry(QtCore.QRect(10, 70, 711, 20))
        self.lineEdit_py.setObjectName("lineEdit")

        self.open_Button = QtWidgets.QPushButton("Save PY File", self.frame)
        self.open_Button.setGeometry(QtCore.QRect(730, 70, 141, 23))
        self.open_Button.clicked.connect(self.save_file)

        self.run_Button1 = QtWidgets.QPushButton("Create *.Py File-1", self.frame)
        self.run_Button1.setGeometry(QtCore.QRect(10, 120, 141, 23))
        self.run_Button1.clicked.connect(self.ui_to_py1)

        self.runpy_Button2 = QtWidgets.QPushButton("Test GUI-1", self.frame)
        self.runpy_Button2.setGeometry(QtCore.QRect(10, 150, 141, 23))
        self.runpy_Button2.clicked.connect(self.test_py_1)

        self.viewpy_Button2 = QtWidgets.QPushButton("View Code Py-1", self.frame)
        self.viewpy_Button2.setGeometry(QtCore.QRect(10, 180, 141, 23))
        self.viewpy_Button2.clicked.connect(self.view_py_1)

        self.run_Button2 = QtWidgets.QPushButton("Create *.Py File-2", self.frame)
        self.run_Button2.setGeometry(QtCore.QRect(160, 120, 141, 23))
        self.run_Button2.clicked.connect(self.ui_to_py2)

        self.runpy_Button2 = QtWidgets.QPushButton("View Code Py-2", self.frame)
        self.runpy_Button2.setGeometry(QtCore.QRect(160, 150, 141, 23))
        self.runpy_Button2.clicked.connect(self.view_py_2)

        self.ext_Button = QtWidgets.QPushButton("Quit", self.frame)
        self.ext_Button.setGeometry(QtCore.QRect(310, 120, 141, 23))
        self.ext_Button.clicked.connect(self.quit_)

        self.about_Button = QtWidgets.QPushButton("About", self.frame)
        self.about_Button.setGeometry(QtCore.QRect(730, 120, 141, 23))
        self.about_Button.clicked.connect(self.about)

        self.show()

    # =====================================================================================================
    # About Info:

    def about(self):
        print("Run Menu About")

        global modalWindow
        modalWindow = QtWidgets.QWidget(window, QtCore.Qt.Window)
        modalWindow.setWindowTitle(" About")
        modalWindow.setGeometry(50, 100, 500, 150)
        modalWindow.setWindowModality(QtCore.Qt.WindowModal)
        modalWindow.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
        #modalWindow.move(window.geometry().center() - modalWindow.rect().center() - QtCore.QPoint(4, 30))

        frame = QtWidgets.QFrame(modalWindow)
        frame.setGeometry(QtCore.QRect(4, 4, 693, 143))
        frame.setFrameShape(QtWidgets.QFrame.Box)
        frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        frame.setObjectName("frame")

        img_label = QtWidgets.QLabel(frame)
        img_label.setGeometry(10, 0, 50, 50)
        pixmap = QPixmap("icon_star.png")
        img_label.setPixmap(pixmap)

        labels = QtWidgets.QLabel(frame)
        labels.setGeometry(10, 30, 250, 80)
        labels.setText(" Converter UI to PY \n\n Data create:  15.07.2021 \n Author edition script:  Bezginov Igory\n This program is free software")

        box1 = QtWidgets.QVBoxLayout()
        box1.addWidget(frame)

        modalWindow.setLayout(box1)
        modalWindow.show()

        print("Finish About")

    # =====================================================================================================
    # Quit Program:

    def quit_(self):
        print("Run Quit Programm")
        quit()

    # =====================================================================================================
    # Open *.ui file:    /Obligatory/

    def open_file(self):
        print("open_file")
        global file

        file, _ = QFileDialog.getOpenFileName(self, caption="Open UI File",
                                              directory="c:/!!!_000_Az_Esm_New_UTM/Prohorenok_QMainWindow_CreateMyMenu/Designer_menu_ui/",
                                              filter="Ui (*.ui)")
        print(file)
        self.lineEdit.setText(file)

        return file

    # =====================================================================================================
    # Save *.py file:    /Not Obligatory/

    def save_file(self):
        print("Run Save_File")
        ui_file, _ = QFileDialog.getSaveFileName(self, caption="Save Py File",
                                              directory="c:/",
                                              filter="Py (*.py;; All (*.*)")

        print(ui_file)
        self.lineEdit_py.setText(ui_file)

    # =====================================================================================================
    # Run 1 Convertation ui to py:          /Start Gui.py/

    def ui_to_py1(self):
        print("Run ui_to_py-1")

        ui_file1 = str(self.lineEdit.text())
        py_file1 = str(self.lineEdit.text()[:-3]) + "_1.py"

        save_file_py = str(self.lineEdit_py.text())
        if save_file_py == "":
            print(ui_file1)
            print(py_file1)

            cmd = (f"pyuic5 -x {ui_file1} -o {py_file1}")
            subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        else:
            print(ui_file1)
            print(save_file_py)
            cmd = (f"pyuic5 -x {ui_file1} -o {save_file_py}")
            subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)

        print("Finish Convertation ui to py-1")
    # =====================================================================================================
    # Run Testing 1-version Gui.py:

    def test_py_1(self):
        print("Run Test Py 1")
        py_file1 = str(self.lineEdit.text()[:-3]) + "_1.py"
        #print(py_file1)

        save_file_py = str(self.lineEdit_py.text())
        if save_file_py == "":
            print(py_file1)
            cmd = (f"python {py_file1}")
            subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        else:
            cmd = (f"python {save_file_py}")
            subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)

        print("Finish Test Py-1")

    # =====================================================================================================
    # Run Viewer Code Testing 1-version Gui.py:            /insert name txt or py editor/

    def view_py_1(self):
        print("Run View_Code_Py-1")

        py_file1 = str(self.lineEdit.text()[:-3]) + "_1.py"
        #print(py_file1)

        save_file_py = str(self.lineEdit_py.text())
        if save_file_py == "":
            print(py_file1)
            cmd = (f"notepad {py_file1}")
            subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        else:
            cmd = (f"notepad {save_file_py}")
            subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)

        print("Finish View_Code_Py-1")

    # =====================================================================================================
    # Run 2 Convertation ui to py:          /Not Start Gui.py/
    def ui_to_py2(self):
        print("Run ui_to_py2")

        ui_file2 = str(self.lineEdit.text())
        py_file2 = str(self.lineEdit.text()[:-3]) + "_2.py"

        save_file_py2 = str(self.lineEdit_py.text())
        if save_file_py2 == "":
            print(ui_file2)
            print(py_file2)
            cmd = (f"pyuic5 {ui_file2} -o {py_file2}")
            subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        else:
            cmd = (f"pyuic5 {ui_file2} -o {save_file_py2}")
            subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)

        print("Finish Convertation ui to py-2")

    # =====================================================================================================
    # Run Viewer Code Testing 2-version Gui.py:            /insert name txt or py editor/

    def view_py_2(self):
        print("Run View_Code_Py-2")

        py_file2 = str(self.lineEdit.text()[:-3]) + "_2.py"
        print(py_file2)

        save_file_py2 = str(self.lineEdit_py.text())
        if save_file_py2 == "":
            cmd = (f"notepad {py_file2}")
            subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        else:
            cmd = (f"notepad {save_file_py2}")
            subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        print("Finish View_Code_Py-2")
    # =====================================================================================================

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())

