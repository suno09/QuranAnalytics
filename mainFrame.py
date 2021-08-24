# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainFrame.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

""" Main window of application """

from PyQt5 import QtCore, QtGui, QtWidgets
from time import time
from showdialog import showdialog
import re
from quran_index import load_data_index_ahkaam_encoding, \
    load_data_index_quran_buckwalter, load_sourats_names
from transliteration import isArabic, isLatin, translit_to_arab, translit_to_latin
from histogram import plot_histogram
from searchEncoding import get_versets_by_encoding
import os


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1060, 599)
        MainWindow.setMinimumSize(QtCore.QSize(1060, 599))
        MainWindow.setMaximumSize(QtCore.QSize(1060, 599))
        MainWindow.setStyleSheet("")
        self.mainWindow = MainWindow
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(240, 10, 811, 511))
        self.tableWidget.setStyleSheet(
            "background-image: url(:/images/imgQuran.png);")
        self.tableWidget.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(10, 530, 1041, 23))
        self.progressBar.setStyleSheet("QProgressBar {\n"
                                       "    border: 2px solid black;\n"
                                       "}\n"
                                       "")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 560, 1041, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel {\n"
                                 "    border: 2px solid black;\n"
                                 "    border-radius: 9px;\n"
                                 "}\n"
                                 "")
        self.label.setText("")
        self.label.setObjectName("label")
        self.gbIndexation = QtWidgets.QGroupBox(self.centralwidget)
        self.gbIndexation.setGeometry(QtCore.QRect(10, 10, 221, 93))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.gbIndexation.setFont(font)
        self.gbIndexation.setStyleSheet("QGroupBox {\n"
                                        "    border: 2px solid black;\n"
                                        "    border-radius: 9px;\n"
                                        "    margin-top: 0.5em;\n"
                                        "}\n"
                                        "QGroupBox::title {\n"
                                        "    subcontrol-origin: margin;\n"
                                        "    left: 10px;\n"
                                        "    padding: -2 3px 0 3px;\n"
                                        "}")
        self.gbIndexation.setObjectName("gbIndexation")
        self.pbNewRecharge = QtWidgets.QPushButton(self.gbIndexation)
        self.pbNewRecharge.setGeometry(QtCore.QRect(10, 55, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pbNewRecharge.setFont(font)
        self.pbNewRecharge.setObjectName("pbNewRecharge")
        self.pbOldRecharge = QtWidgets.QPushButton(self.gbIndexation)
        self.pbOldRecharge.setGeometry(QtCore.QRect(10, 20, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pbOldRecharge.setFont(font)
        self.pbOldRecharge.setObjectName("pbOldRecharge")
        self.gbOperation = QtWidgets.QGroupBox(self.centralwidget)
        self.gbOperation.setEnabled(False)
        self.gbOperation.setGeometry(QtCore.QRect(10, 110, 221, 341))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.gbOperation.setFont(font)
        self.gbOperation.setStyleSheet("QGroupBox {\n"
                                       "    border: 2px solid black;\n"
                                       "    border-radius: 9px;\n"
                                       "    margin-top: 0.5em;\n"
                                       "}\n"
                                       "QGroupBox::title {\n"
                                       "    subcontrol-origin: margin;\n"
                                       "    left: 10px;\n"
                                       "    padding: -2 3px 0 3px;\n"
                                       "}")
        self.gbOperation.setObjectName("gbOperation")
        self.cbOperation = QtWidgets.QComboBox(self.gbOperation)
        self.cbOperation.setGeometry(QtCore.QRect(10, 20, 201, 24))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cbOperation.setFont(font)
        self.cbOperation.setObjectName("cbOperation")
        self.cbOperation.addItem("")
        self.cbOperation.addItem("")
        self.cbOperation.addItem("")
        self.cbOperation.addItem("")
        self.rbFromTexte = QtWidgets.QRadioButton(self.gbOperation)
        self.rbFromTexte.setGeometry(QtCore.QRect(10, 50, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.rbFromTexte.setFont(font)
        self.rbFromTexte.setCheckable(True)
        self.rbFromTexte.setChecked(True)
        self.rbFromTexte.setObjectName("rbFromTexte")
        self.gbAPartirQuran = QtWidgets.QGroupBox(self.gbOperation)
        self.gbAPartirQuran.setGeometry(QtCore.QRect(10, 100, 201, 191))
        self.gbAPartirQuran.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(10)
        self.gbAPartirQuran.setFont(font)
        self.gbAPartirQuran.setAutoFillBackground(False)
        self.gbAPartirQuran.setStyleSheet("QGroupBox {\n"
                                          "    border: 2px solid black;\n"
                                          "    border-radius: 9px;\n"
                                          "    margin-top: 0.5em;\n"
                                          "}\n"
                                          "QGroupBox::title {\n"
                                          "    subcontrol-origin: margin;\n"
                                          "    left: 10px;\n"
                                          "    padding: -2 3px 0 3px;\n"
                                          "}")
        self.gbAPartirQuran.setCheckable(False)
        self.gbAPartirQuran.setChecked(False)
        self.gbAPartirQuran.setObjectName("gbAPartirQuran")
        self.gbSourat = QtWidgets.QGroupBox(self.gbAPartirQuran)
        self.gbSourat.setGeometry(QtCore.QRect(10, 20, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(10)
        self.gbSourat.setFont(font)
        self.gbSourat.setAutoFillBackground(False)
        self.gbSourat.setStyleSheet("QGroupBox {\n"
                                    "    border: 2px solid gray;\n"
                                    "    border-radius: 9px;\n"
                                    "    margin-top: 0.5em;\n"
                                    "}\n"
                                    "QGroupBox::title {\n"
                                    "    subcontrol-origin: margin;\n"
                                    "    left: 10px;\n"
                                    "    padding: -2 3px 0 3px;\n"
                                    "}")
        self.gbSourat.setCheckable(False)
        self.gbSourat.setChecked(False)
        self.gbSourat.setObjectName("gbSourat")
        self.cbNomSourat = QtWidgets.QComboBox(self.gbSourat)
        self.cbNomSourat.setGeometry(QtCore.QRect(10, 20, 161, 24))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cbNomSourat.setFont(font)
        self.cbNomSourat.setObjectName("cbNomSourat")
        self.gbVersetMin = QtWidgets.QGroupBox(self.gbAPartirQuran)
        self.gbVersetMin.setGeometry(QtCore.QRect(10, 75, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(10)
        self.gbVersetMin.setFont(font)
        self.gbVersetMin.setAutoFillBackground(False)
        self.gbVersetMin.setStyleSheet("QGroupBox {\n"
                                       "    border: 2px solid gray;\n"
                                       "    border-radius: 9px;\n"
                                       "    margin-top: 0.5em;\n"
                                       "}\n"
                                       "QGroupBox::title {\n"
                                       "    subcontrol-origin: margin;\n"
                                       "    left: 10px;\n"
                                       "    padding: -2 3px 0 3px;\n"
                                       "}")
        self.gbVersetMin.setCheckable(False)
        self.gbVersetMin.setChecked(False)
        self.gbVersetMin.setObjectName("gbVersetMin")
        self.cbVersetMin = QtWidgets.QComboBox(self.gbVersetMin)
        self.cbVersetMin.setGeometry(QtCore.QRect(10, 20, 161, 24))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cbVersetMin.setFont(font)
        self.cbVersetMin.setObjectName("cbVersetMin")
        self.gbVersetMax = QtWidgets.QGroupBox(self.gbAPartirQuran)
        self.gbVersetMax.setGeometry(QtCore.QRect(10, 130, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(10)
        self.gbVersetMax.setFont(font)
        self.gbVersetMax.setAutoFillBackground(False)
        self.gbVersetMax.setStyleSheet("QGroupBox {\n"
                                       "    border: 2px solid gray;\n"
                                       "    border-radius: 9px;\n"
                                       "    margin-top: 0.5em;\n"
                                       "}\n"
                                       "QGroupBox::title {\n"
                                       "    subcontrol-origin: margin;\n"
                                       "    left: 10px;\n"
                                       "    padding: -2 3px 0 3px;\n"
                                       "}")
        self.gbVersetMax.setCheckable(False)
        self.gbVersetMax.setChecked(False)
        self.gbVersetMax.setObjectName("gbVersetMax")
        self.cbVersetMax = QtWidgets.QComboBox(self.gbVersetMax)
        self.cbVersetMax.setGeometry(QtCore.QRect(10, 20, 161, 24))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cbVersetMax.setFont(font)
        self.cbVersetMax.setObjectName("cbVersetMax")
        self.rbFromQuran = QtWidgets.QRadioButton(self.gbOperation)
        self.rbFromQuran.setGeometry(QtCore.QRect(10, 75, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.rbFromQuran.setFont(font)
        self.rbFromQuran.setObjectName("rbFromQuran")
        self.pbRequete = QtWidgets.QPushButton(self.gbOperation)
        self.pbRequete.setEnabled(False)
        self.pbRequete.setGeometry(QtCore.QRect(10, 300, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pbRequete.setFont(font)
        self.pbRequete.setObjectName("pbRequete")
        self.pbSave = QtWidgets.QPushButton(self.centralwidget)
        self.pbSave.setEnabled(False)
        self.pbSave.setGeometry(QtCore.QRect(20, 457, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pbSave.setFont(font)
        self.pbSave.setObjectName("pbSave")
        self.pbQuitter = QtWidgets.QPushButton(self.centralwidget)
        self.pbQuitter.setGeometry(QtCore.QRect(20, 490, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pbQuitter.setFont(font)
        self.pbQuitter.setObjectName("pbQuitter")
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionBooleen = QtWidgets.QAction(MainWindow)
        self.actionBooleen.setObjectName("actionBooleen")
        self.actionVectoriel = QtWidgets.QAction(MainWindow)
        self.actionVectoriel.setObjectName("actionVectoriel")
        self.actionIndex = QtWidgets.QAction(MainWindow)
        self.actionIndex.setObjectName("actionIndex")
        self.actionInverse = QtWidgets.QAction(MainWindow)
        self.actionInverse.setObjectName("actionInverse")

        self.retranslateUi(MainWindow)
        self.pbOldRecharge.clicked.connect(lambda: self.reload_old())
        self.pbNewRecharge.clicked.connect(lambda: self.reload_new())
        self.rbFromTexte.toggled.connect(
            lambda: self.gbAPartirQuran.setEnabled(False))
        self.rbFromQuran.toggled.connect(
            lambda: self.gbAPartirQuran.setEnabled(True))
        self.cbNomSourat.currentIndexChanged['int'].connect(
            lambda x: self.set_verset_min_max(x))
        self.cbOperation.currentIndexChanged['int'].connect(
            lambda x: self.choose_operation(x))
        self.pbQuitter.clicked.connect(lambda: self.quitter())
        self.pbRequete.clicked.connect(lambda: self.operation())
        self.pbSave.clicked.connect(lambda: self.save_result())

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def choose_operation(self, oper):
        if oper == 0:
            self.rbFromTexte.setChecked(True)
            self.rbFromTexte.setEnabled(True)
            self.rbFromQuran.setEnabled(True)
            self.gbAPartirQuran.setEnabled(False)
        elif oper == 1:
            self.rbFromTexte.setEnabled(False)
            self.rbFromTexte.setChecked(False)
            self.rbFromQuran.setEnabled(False)
            self.gbAPartirQuran.setEnabled(False)
        elif oper == 2:
            self.rbFromTexte.setEnabled(False)
            self.rbFromQuran.setEnabled(True)
            self.rbFromQuran.setChecked(True)
            self.gbAPartirQuran.setEnabled(True)
        else:
            self.rbFromTexte.setEnabled(True)
            self.rbFromTexte.setChecked(True)
            self.rbFromQuran.setEnabled(False)
            self.gbAPartirQuran.setEnabled(False)
        self.pbSave.setEnabled(False)

    def operation(self):
        self.progressBar.setRange(0, 0)
        self.label.setText("")
        self.pbSave.setEnabled(False)
        # transliteration
        if self.cbOperation.currentIndex() == 0:
            text_to = ''
            text_translit = ''
            self.text_save = """Translitération\n"""
            # si texte
            if self.rbFromTexte.isChecked():
                requete, ok = QtWidgets. \
                    QInputDialog.getText(None,
                                         "Transliteration",
                                         "Insert text to transliterate it")
                if ok:
                    startt = time()
                    if not requete.strip():
                        showdialog(QtWidgets.QMessageBox.Critical, 'Error',
                                   'Insert a text in Arabic or Latin !')
                        text_from = ''
                        self.progressBar.setRange(0, 100)
                        self.progressBar.setValue(0)
                        self.label.setText("")
                    elif isArabic(requete):
                        text_translit = translit_to_latin(requete)
                        text_from = 'Arabic'
                        text_to = 'Latin'
                    elif isLatin(requete):
                        text_translit = translit_to_arab(requete)
                        text_from = 'Latin'
                        text_to = 'Arabic'
                    else:
                        showdialog(QtWidgets.QMessageBox.Critical, 'Error',
                                   'Insert a text in Arabic or Latin !')
                        text_from = ''
                        self.progressBar.setRange(0, 100)
                        self.progressBar.setValue(0)
                        self.label.setText("")
                    endt = time()
                    # affichage resultat
                    if text_from:
                        self.tableWidget.setRowCount(0)
                        self.tableWidget.setStyleSheet("")
                        self.tableWidget.setColumnCount(1)
                        self.tableWidget.setRowCount(2)
                        self.tableWidget. \
                            horizontalHeader().setDefaultSectionSize(750)
                        item = QtWidgets.QTableWidgetItem()
                        item.setText(text_from + " to " + text_to)
                        self.text_save += text_from + " to " + text_to + "\n"
                        self.tableWidget.setHorizontalHeaderItem(0, item)
                        item = QtWidgets.QTableWidgetItem()
                        item.setText(text_from)
                        self.tableWidget.setVerticalHeaderItem(0, item)
                        item = QtWidgets.QTableWidgetItem()
                        item.setText(text_to)
                        self.tableWidget.setVerticalHeaderItem(1, item)
                        item = QtWidgets.QTextEdit()
                        item.setReadOnly(True)
                        item.setText(requete)
                        self.tableWidget.setCellWidget(0, 0, item)
                        item = QtWidgets.QTextEdit()
                        item.setReadOnly(True)
                        item.setText(text_translit)
                        self.text_save += requete + "\n" + text_translit + "\n"
                        self.tableWidget.setCellWidget(1, 0, item)
                        self.label.setText(
                            'Operation completed in %.2f seconds' % (
                                    endt - startt))
                        self.progressBar.setRange(0, 100)
                        self.progressBar.setValue(100)
                        self.pbSave.setEnabled(True)
                else:
                    self.progressBar.setRange(0, 100)
                    self.progressBar.setValue(0)
            else:
                # transliteration a partir quran
                deb = int(self.cbVersetMin.currentText())
                fin = int(self.cbVersetMax.currentText())

                if deb > fin:
                    showdialog(QtWidgets.QMessageBox.Critical, 'Error',
                               'Set a correct interval !')
                    self.progressBar.setRange(0, 100)
                    self.progressBar.setValue(0)
                    self.label.setText("")
                else:
                    startt = time()
                    self.tableWidget.setRowCount(0)
                    self.tableWidget.setStyleSheet("")
                    self.tableWidget.setColumnCount(4)
                    self.tableWidget.setRowCount(2 * (fin - deb + 1))
                    self.tableWidget.setColumnWidth(0, 60)
                    self.tableWidget.setColumnWidth(1, 60)
                    self.tableWidget.setColumnWidth(2, 60)
                    self.tableWidget.horizontalHeader().setStretchLastSection(
                        True)
                    item = QtWidgets.QTableWidgetItem()
                    item.setText(self.cbNomSourat.currentText())
                    self.tableWidget.setHorizontalHeaderLabels(
                        ['Sourat', 'Sourat\nnumber', 'Verset', 'Context'])
                    self.text_save += 'Sourat : %s\nSourate number : %s\nVerset | Context\n-----------------\n' \
                                      % (self.sourats_names[
                                             self.cbNomSourat.currentIndex()],
                                         self.cbNomSourat.currentText()[0])
                    item = QtWidgets.QTableWidgetItem()
                    item.setText(
                        self.sourats_names[self.cbNomSourat.currentIndex()])
                    self.tableWidget.setItem(0, 0, item)
                    self.tableWidget.setSpan(0, 0, 2 * (fin - deb + 1), 1)
                    item = QtWidgets.QTableWidgetItem()
                    item.setText(self.cbNomSourat.currentText().split(' - ')[0])
                    self.tableWidget.setItem(0, 1, item)
                    self.tableWidget.setSpan(0, 1, 2 * (fin - deb + 1), 1)
                    for i in range(deb, fin + 1):
                        QtWidgets.QApplication.processEvents()
                        key_quran = self.num_sourats[
                                        self.cbNomSourat.currentIndex()
                                    ] + ":" + "{0:0>3}".format(str(i))
                        text = ' '.join([self.quran[key][0] for key in
                                         sorted(self.quran.keys())
                                         if key.startswith(key_quran)])
                        item = QtWidgets.QTableWidgetItem()
                        item.setText(str(i))
                        self.tableWidget.setItem((i - deb) * 2, 2, item)
                        self.tableWidget.setSpan((i - deb) * 2, 2, 2, 1)
                        item = QtWidgets.QTextEdit()
                        item.setReadOnly(True)
                        item.setText(translit_to_arab(text))
                        self.tableWidget.setCellWidget((i - deb) * 2, 3, item)
                        item = QtWidgets.QTextEdit()
                        item.setReadOnly(True)
                        item.setText(text)
                        self.tableWidget.setCellWidget((i - deb) * 2 + 1, 3,
                                                       item)
                        self.text_save += '%6s | %s\n%6s | %s\n' % \
                                          (
                                              str(i), translit_to_arab(text), '',
                                              text)
                    self.label.setText(
                        'Operation completed in %.2f seconds' % (
                                time() - startt))
                    self.progressBar.setRange(0, 100)
                    self.progressBar.setValue(100)
                    self.pbSave.setEnabled(True)
        # concordanceur
        elif self.cbOperation.currentIndex() == 1:
            from concordancerFrame import ConcordancerFrame
            self.cif = ConcordancerFrame(self)
            self.mainWindow.setEnabled(False)
            self.mw = QtWidgets.QMainWindow()
            self.cif.setupUi(self.mw)
            self.mw.show()
        # Histogramme
        elif self.cbOperation.currentIndex() == 2:
            deb = int(self.cbVersetMin.currentText())
            fin = int(self.cbVersetMax.currentText())

            if deb > fin:
                showdialog(QtWidgets.QMessageBox.Critical, 'Error',
                           'Set a correct interval !')
                self.progressBar.setRange(0, 100)
                self.progressBar.setValue(0)
                self.label.setText("")
            else:
                self.label.setText("Please wait !")
                startt = time()
                self.tableWidget.setStyleSheet("")
                self.tableWidget.setRowCount(0)
                self.tableWidget.setColumnCount(0)
                plot_histogram(
                    self.sourats_names[self.cbNomSourat.currentIndex()],
                    int(self.cbNomSourat.currentText().split(' - ')[0]), deb,
                    fin,
                    self.quran, self.ahkaam, self)
                self.label.setText(
                    'Operation completed in %.2f seconds' % (time() - startt))
                self.progressBar.setRange(0, 100)
                self.progressBar.setValue(100)
                self.pbSave.setEnabled(True)
        # Ahkaam Encoding
        else:
            self.text_save = []
            if self.rbFromTexte.isChecked():
                requete, ok = QtWidgets \
                    .QInputDialog.getText(None,
                                          "Ahkaam Encoding",
                                          "Insert an Ahkaam encoding sequence")
                if ok:
                    encode = requete.strip()
                    self.req = encode
                    if not encode:
                        showdialog(QtWidgets.QMessageBox.Critical, 'Error',
                                   'Insert an encoding sequence of Ahkaam!')
                        self.progressBar.setRange(0, 100)
                        self.progressBar.setValue(0)
                        self.label.setText("")
                    elif not re.match(r'[01246]+', encode):
                        showdialog(QtWidgets.QMessageBox.Critical,
                                   'Error',
                                   "The encoding must be sequences of digits of [0, 1, 2, 4, 5, 6]")
                        self.progressBar.setRange(0, 100)
                        self.progressBar.setValue(0)
                        self.label.setText("")
                    else:
                        self.label.setText(
                            "Please wait...")
                        self.text_save = []
                        get_versets_by_encoding(encode, self.quran, self.ahkaam,
                                                self)

    def save_result(self):
        if self.cbOperation.currentIndex() == 0 or self.cbOperation.currentIndex() == 1:
            options = QtWidgets.QFileDialog.Options()
            options |= QtWidgets.QFileDialog.DontUseNativeDialog
            file_name, _ = QtWidgets.QFileDialog.getSaveFileName(
                self.mainWindow,
                "Save Result",
                "",
                "All files (*);;Text files (*.txt)",
                options=options)
            if file_name:
                with open(file_name, 'w', encoding='utf-8') as f:
                    f.write(self.text_save)
                showdialog(QtWidgets.QMessageBox.Information, 'Succees',
                           'Operation completed successfully')
        elif self.cbOperation.currentIndex() == 2:
            folder_name = 'histogram_' \
                          + str(self.cbNomSourat.currentIndex() + int(
                sorted(self.ahkaam.keys())[0])) \
                          + '_' + self.cbVersetMin.currentText() \
                          + '_' + self.cbVersetMax.currentText()
            try:
                os.makedirs(folder_name)
                self.label.setText('Please wait...')
                self.progressBar.setRange(0, 0)
                for i in range(len(self.text_save)):
                    QtWidgets.QApplication.processEvents()
                    self.text_save[i].savefig(folder_name + '/' + str(
                        i + int(self.cbVersetMin.currentText())) + '.png')
                self.progressBar.setRange(0, 100)
                self.progressBar.setValue(100)
                self.label.setText(
                    "Le résultat a été sauvegardé dans le répertoire " +
                    folder_name)
            except:
                showdialog(QtWidgets.QMessageBox.Critical, 'Error',
                           "Folder " + folder_name + " exists !")
        # sauvegarder search encoding
        else:
            folder_name = 'search_encoding_' + self.req
            try:
                os.makedirs(folder_name)
                self.label.setText('Please wait...')
                self.progressBar.setRange(0, 0)
                ind = 0
                for i in sorted(self.listResult2.keys()):
                    QtWidgets.QApplication.processEvents()
                    for j in sorted(self.listResult2[i].keys()):
                        QtWidgets.QApplication.processEvents()
                        self.text_save[ind].savefig(
                            folder_name + '/' + i + '_' + j + '.png')
                        ind += 1
                with open(folder_name + '/' + folder_name + '.txt', 'w',
                          encoding='utf-8') as w:
                    w.write(self.textSave2)
                self.progressBar.setRange(0, 100)
                self.progressBar.setValue(100)
                self.label.setText(
                    "The result has been saved in the directory" + folder_name)
            except:
                showdialog(QtWidgets.QMessageBox.Critical, 'Error',
                           "Folder " + folder_name + " exists !")

    def set_verset_min_max(self, x):
        self.cbVersetMax.clear()
        self.cbVersetMin.clear()
        self.cbVersetMin.addItems(
            list(map(str, range(1, len(self.ahkaam[self.num_sourats[x]]) + 1))))
        self.cbVersetMax.addItems(
            list(map(str, range(1, len(self.ahkaam[self.num_sourats[x]]) + 1))))

    def reload_new(self):
        from chargeIndexFrame import ChargeIndexFrame
        self.cif = ChargeIndexFrame(self)
        self.mainWindow.setEnabled(False)
        self.mw = QtWidgets.QMainWindow()
        self.cif.setupUi(self.mw)
        self.mw.show()

    def reload_old(self):
        self.progressBar.setRange(0, 0)
        self.label.setText("Chargement des Indexs Quran et Ahkaam...")
        startt = time()
        self.quran = load_data_index_quran_buckwalter()
        self.ahkaam = load_data_index_ahkaam_encoding()
        self.num_sourats = sorted(self.ahkaam.keys())
        self.sourats_names = load_sourats_names()[
                            int(self.num_sourats[0]) - 1:int(
                                self.num_sourats[-1])]
        self.cbNomSourat.clear()
        self.cbVersetMin.clear()
        self.cbVersetMax.clear()
        for i in self.num_sourats:
            QtWidgets.QApplication.processEvents()
            self.cbNomSourat.addItem(str(int(i)) + ' - ' + self.sourats_names[
                abs(int(self.num_sourats[0]) - int(i))])
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setStyleSheet(
            "background-image: url(:/images/imgQuran.png);")
        self.label.setText(
            "The Quran and Ahkaam Indexes were loaded in %.2f seconds" % (
                    time() - startt))
        self.gbOperation.setEnabled(True)
        self.pbRequete.setEnabled(True)
        self.progressBar.setRange(0, 100)
        self.progressBar.setValue(100)

    def quitter(self):
        quit_msg = "Are you sure you want to quit ?"
        reply = QtWidgets.QMessageBox.question(self.mainWindow, 'Go out !',
                                               quit_msg,
                                               QtWidgets.QMessageBox.Yes,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            self.mainWindow.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(
            _translate("MainWindow",
                       "Implementation of a tool for stylometric analysis of the Quran"))
        self.gbIndexation.setTitle(_translate("MainWindow", "Indexation"))
        self.pbNewRecharge.setText(
            _translate("MainWindow", "Loading the new Index"))
        self.pbOldRecharge.setText(
            _translate("MainWindow", "Loading the old Index"))
        self.gbOperation.setTitle(_translate("MainWindow", "Operation"))
        self.cbOperation.setItemText(0, _translate("MainWindow",
                                                   "Transliteration"))
        self.cbOperation.setItemText(1,
                                     _translate("MainWindow", "Concordance"))
        self.cbOperation.setItemText(2, _translate("MainWindow", "Histogram"))
        self.cbOperation.setItemText(3, _translate("MainWindow",
                                                   "Encoding search"))
        self.rbFromTexte.setText(_translate("MainWindow", "Manually"))
        self.gbAPartirQuran.setTitle(
            _translate("MainWindow", "Automatically"))
        self.gbSourat.setTitle(_translate("MainWindow", "Sourat"))
        self.gbVersetMin.setTitle(_translate("MainWindow", "Verset Minimum"))
        self.gbVersetMax.setTitle(_translate("MainWindow", "Verset Maximum"))
        self.rbFromQuran.setText(_translate("MainWindow", "Coran"))
        self.pbRequete.setText(_translate("MainWindow", "Start"))
        self.pbSave.setText(
            _translate("MainWindow", "Save Results"))
        self.pbQuitter.setText(_translate("MainWindow", "Leave"))
        self.actionBooleen.setText(_translate("MainWindow", "Booleen"))
        self.actionVectoriel.setText(_translate("MainWindow", "Vectoriel"))
        self.actionIndex.setText(_translate("MainWindow", "Index"))
        self.actionIndex.setToolTip(_translate("MainWindow", "Show index"))
        self.actionInverse.setText(_translate("MainWindow", "Reverse"))
        self.actionInverse.setToolTip(
            _translate("MainWindow", "Show reverse"))


import imgQuran_rc

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
