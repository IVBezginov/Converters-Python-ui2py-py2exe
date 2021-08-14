# -*- coding: utf-8 -*-
# Converter Py to Exe
# Create script 16.07.2021
# Author edition script: Bezginov Igory
# This program is free software

"""
Python-3
Install  Modules PyQt5, pyinstaller

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

        self.title = " Converter PY to EXE"
        self.top = 100
        self.left = 100
        self.width = 900
        self.height = 240

        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("icon_star.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)

        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(10, 10, 881, 201))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")

        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(10, 20, 711, 20))
        self.lineEdit.setObjectName("lineEdit")

        self.open_Button = QtWidgets.QPushButton("Open *.Py File", self.frame)
        self.open_Button.setGeometry(QtCore.QRect(730, 20, 141, 23))
        self.open_Button.clicked.connect(self.open_file)

        self.run_Button = QtWidgets.QPushButton("Create *.exe File", self.frame)
        self.run_Button.setGeometry(QtCore.QRect(10, 120, 141, 23))
        self.run_Button.clicked.connect(self.py_to_exe)

        self.run_Button2 = QtWidgets.QPushButton("Run *.exe File", self.frame)
        self.run_Button2.setGeometry(QtCore.QRect(160, 120, 141, 23))
        self.run_Button2.clicked.connect(self.run_exe_file)

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
        labels.setGeometry(10, 35, 250, 80)
        labels.setText("Py_2_Exe\n\n Converter Py-script to *.exe-file \n Data create:  16.07.2021 \n Author edition script:  Bezginov Igory\n This program is free software")

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
        print("Run open_file")
        global file

        file, _ = QFileDialog.getOpenFileName(self, caption="Open Py File",
                                              directory="c:/!!!_000_Az/",
                                              filter="Py (*.py)")
        print(file)
        self.lineEdit.setText(file)

        return file

    # =====================================================================================================
    # Run Convertation py to exe:

    def py_to_exe(self):
        print("Run py_to_exe")

        py_file = str(self.lineEdit.text())
        print(py_file)

        cmd = (f"pyinstaller {py_file}")
        subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)

        print("Finish Convertation py to exe")
    # =====================================================================================================
    # Run Testing *.exe File:

    def run_exe_file(self):
        print("Run *.exe File")
        from pathlib import Path

        path_file_name = (self.lineEdit.text())
        pfn = Path(path_file_name)
        print(pfn)

        exe_file = str(pfn.parent) + "/dist/" + str(pfn.stem) + "/" + str(pfn.stem) + ".exe"
        print(exe_file)

        import os
        os.startfile(str(exe_file))

        print("Finish Run *.exe File")

    # =====================================================================================================

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())

