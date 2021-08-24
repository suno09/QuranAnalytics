# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chargeIndexFrame.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from quran_index import generate_index_quran_buckwalter, \
    generate_index_ahkaam_encoding
from showdialog import showdialog
from time import time


class ChargeIndexFrame(object):

    def cancel(self):
        self.frameFather.mainWindow.setEnabled(True)
        self.MainWindow.close()

    def generate(self):
        start = int(self.cbDebut.currentText())
        end = int(self.cbFin.currentText())

        if start > end:
            showdialog(QtWidgets.QMessageBox.Critical, 'Error',
                       'Set a correct interval !')
        else:
            start_time = time()
            self.frameFather.label.setText(
                "Loading the new Quran index...")
            self.frameFather.progressBar.setRange(0, 0)
            self.MainWindow.setEnabled(False)
            generate_index_quran_buckwalter(start, end, self.frameFather)
            generate_index_ahkaam_encoding(start, end, self.frameFather)
            self.frameFather.reload_old()
            self.frameFather.progressBar.setRange(0, 100)
            self.frameFather.progressBar.setValue(100)
            self.frameFather.label.setText(
                "Loading of Quran and Ahkaam indexes completed: % .2f seconds"
                % (time() - start_time))
            self.MainWindow.setEnabled(True)
            showdialog(QtWidgets.QMessageBox.Information,
                       'Generation of indexes',
                       'Operation completed successfully ^_^')
        self.frameFather.mainWindow.setEnabled(True)
        self.MainWindow.close()

    def __init__(self, arg):
        super(ChargeIndexFrame, self).__init__()
        self.frameFather = arg

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(356, 107)
        self.MainWindow = MainWindow
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setGeometry(QtCore.QRect(50, 70, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.buttonBox.setFont(font)
        self.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gbDebut = QtWidgets.QGroupBox(self.centralwidget)
        self.gbDebut.setGeometry(QtCore.QRect(10, 10, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.gbDebut.setFont(font)
        self.gbDebut.setObjectName("gbDebut")
        self.cbDebut = QtWidgets.QComboBox(self.gbDebut)
        self.cbDebut.setGeometry(QtCore.QRect(10, 20, 141, 22))
        self.cbDebut.setObjectName("cbDebut")
        self.gbFin = QtWidgets.QGroupBox(self.centralwidget)
        self.gbFin.setGeometry(QtCore.QRect(190, 10, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.gbFin.setFont(font)
        self.gbFin.setObjectName("gbFin")
        self.cbFin = QtWidgets.QComboBox(self.gbFin)
        self.cbFin.setGeometry(QtCore.QRect(10, 20, 141, 22))
        self.cbFin.setObjectName("cbFin")
        MainWindow.setCentralWidget(self.centralwidget)

        for i in range(114):
            self.cbDebut.addItem(str(i + 1))
            self.cbFin.addItem(str(i + 1))

        self.retranslateUi(MainWindow)
        self.buttonBox.rejected.connect(lambda: self.cancel())
        self.buttonBox.accepted.connect(lambda: self.generate())
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(
            _translate("MainWindow", "Loading New Quran and Ahkaam Index"))
        self.gbDebut.setTitle(_translate("MainWindow", "Sourat Start"))
        self.gbFin.setTitle(_translate("MainWindow", "Sourat End"))
