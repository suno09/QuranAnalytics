# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'concordanceurFrame.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

""" Search for matches and context of a certain word """

from PyQt5 import QtCore, QtGui, QtWidgets
from showdialog import showdialog
from transliteration import isLatin, isArabic, translit_to_latin, \
    translit_to_arab, unicodeTextLatin
from concordancer import concordancer
from time import time
import re
import html
import urllib


class ConcordancerFrame(object):
    def cancel(self):
        self.frameFather.mainWindow.setEnabled(True)
        self.frameFather.progressBar.setRange(0, 100)
        self.frameFather.progressBar.setValue(0)
        self.MainWindow.close()

    def generate(self):
        self.MainWindow.setEnabled(False)
        requete = self.textEdit.toPlainText().strip()
        self.frameFather.label.setText('Please wait...')
        text_from = '1'
        if requete.strip() == '':
            showdialog(QtWidgets.QMessageBox.Critical, 'Error',
                       'Enter a word to search')
            text_from = ''
            self.MainWindow.setEnabled(True)
        elif isArabic(requete):
            text_translit = translit_to_latin(requete)
            url_text = text_translit
        elif isLatin(requete):
            text_translit = requete
            url_text = text_translit
        else:
            showdialog(QtWidgets.QMessageBox.Critical, 'Error',
                       'Insert a text in Arabic or Latin !')
            text_from = ''
            self.frameFather.progressBar.setRange(0, 100)
            self.frameFather.progressBar.setValue(0)
            self.MainWindow.setEnabled(True)
        if text_from != '':
            startt = time()
            # affichage resultat
            list_results = concordancer(self.frameFather.quran, text_translit,
                                        self.cbTypeSearch.currentText(),
                                        self.cbNbrWords.currentText())
            # fint = time()
            result = True
            if not list_results:
                text = text_translit[0]
                for i in range(1, len(text_translit) - 1):
                    QtWidgets.QApplication.processEvents()
                    if text_translit[i] != 'A':
                        text += text_translit[i]
                text_translit = text + text_translit[-1]
                list_results = concordancer(self.frameFather.quran,
                                            text_translit,
                                            self.cbTypeSearch.currentText(),
                                            self.cbNbrWords.currentText())
                # fint = time()
                if not list_results:
                    showdialog(QtWidgets.QMessageBox.Critical, 'Error',
                               'No results were found !')
                    self.frameFather.progressBar.setRange(0, 100)
                    self.frameFather.progressBar.setValue(0)
                    self.frameFather.label.setText(
                        'Operation completed in %.2f seconds' % (
                                    time() - startt))
                    result = False
                    self.MainWindow.setEnabled(True)
            if result:
                # calculer precision et rappel et f_score
                pattern1 = r'(?:<td.+?(?:</td>)){2}<td.+?>.+?</td.*?>' \
                           r'<td.+?>.+?</td.*?>'
                pattern2 = r'(<td.+?(</td>)){2}<td.+?>(.+?)</td.*?>' \
                           r'<td.+?>(.+?)</td.*?>'
                unicode_text_translit = unicodeTextLatin(url_text)
                i = 1
                nbr_doc_pertinent = 0
                nbr_doc_pertinent_env = 0
                while True:
                    try:
                        QtWidgets.QApplication.processEvents()
                        self.frameFather.label.setText('Process page ' + str(
                            i) + ' ! Please wait...')
                        url = 'http://qurancomplex.gov.sa/quran/Search/' \
                              'hits.asp?l=arb&wordtxtsrch=%s&SType=RootMode&' \
                              'AndOr=Anding&Seq=Sequential&Start=%d&Adv=1' % (
                                  unicode_text_translit, i)
                        page_code = urllib.request.urlopen(url).read().decode(
                            'ISO-8859-1')
                        index = re.findall(pattern1, page_code)
                        if index:
                            nbr_doc_pertinent_env += len(index)
                            for ind in index:
                                QtWidgets.QApplication.processEvents()
                                str_verset = re.search(pattern2, ind)
                                if "{0:0>3}".format(
                                        int(str_verset.group(3))) + ":" + \
                                        "{0:0>3}".format(int(str_verset.group(
                                            4))) in list_results.keys():
                                    nbr_doc_pertinent += 1
                        else:
                            break
                        i += 1
                    except:
                        showdialog(QtWidgets.QMessageBox.Critical,
                                   'Error',
                                   "Problem in URL or connection\n(Precision, "
                                   "Recall and F_score will not count)")
                        break
                if nbr_doc_pertinent_env != 0:
                    p = nbr_doc_pertinent / len(list_results)
                    r = nbr_doc_pertinent / nbr_doc_pertinent_env
                    f_score = 2 * p * r / (p + r)
                else:
                    p = r = f_score = 0
                endt = time()
                self.frameFather.tableWidget.setRowCount(0)
                self.frameFather.tableWidget.setStyleSheet("")
                self.frameFather.tableWidget.setColumnCount(4)
                self.frameFather.tableWidget.setRowCount(
                    len(list_results) * 2 + 1)
                self.frameFather.tableWidget.setColumnWidth(0, 60)
                self.frameFather.tableWidget.setColumnWidth(1, 60)
                self.frameFather.tableWidget.setColumnWidth(2, 60)
                self.frameFather \
                    .tableWidget \
                    .horizontalHeader() \
                    .setStretchLastSection(True)
                self.frameFather.tableWidget.setHorizontalHeaderLabels(
                    ['Sourat', 'Sourat\nnumber', 'Verset', 'Context'])
                self.frameFather.text_save = 'Concordancer\nSearch word : %s\nSearch type : %s\n' \
                                             'Number of Words before and after word found : %d\n' \
                                             'Verse number found : %d verset(s)\n' \
                                             'Word number found : %d word(s)\n' \
                                             "Precision : %f\n" \
                                             "Recall : %f\n" \
                                             "F-Score : %f\n\n" % (
                                                 requete,
                                                 self.cbTypeSearch.currentText(),
                                                 self.cbNbrWords.currentIndex(),
                                                 len(list_results),
                                                 sum([len(liste[0]) for liste in
                                                      list_results.values()]),
                                                 p, r, f_score)
                self.frameFather.text_save += '     Sourat    | Sourat number | Verset | Context ' \
                                              '\n' + ('-' * 51) + '\n'
                i = 0
                ind_first_sourat = int(
                    sorted(self.frameFather.ahkaam.keys())[0])
                for key, lists in sorted(list_results.items(),
                                         key=lambda x: x[0]):
                    QtWidgets.QApplication.processEvents()
                    item = QtWidgets.QTableWidgetItem()
                    item.setText(self.frameFather.sourats_names[
                                     int(key[:3]) - ind_first_sourat])
                    self.frameFather.tableWidget.setItem(i * 2, 0, item)
                    self.frameFather.tableWidget.setSpan(i * 2, 0, 2, 1)
                    item = QtWidgets.QTableWidgetItem()
                    item.setText(str(int(key[:3])))
                    self.frameFather.tableWidget.setItem(i * 2, 1, item)
                    self.frameFather.tableWidget.setSpan(i * 2, 1, 2, 1)
                    item = QtWidgets.QTableWidgetItem()
                    item.setText(str(int(key[4:])))
                    self.frameFather.tableWidget.setItem(i * 2, 2, item)
                    self.frameFather.tableWidget.setSpan(i * 2, 2, 2, 1)
                    span = "<span style=\" color:red;\" >"
                    end_span = "</span>"
                    text_latin = """"""
                    text_latin_save = ""
                    text_arab = ""
                    text_arab_save = ""
                    for num_pos_word in lists[1]:
                        QtWidgets.QApplication.processEvents()
                        if num_pos_word in lists[0]:
                            text_arab += span + translit_to_arab(
                                self.frameFather.quran[num_pos_word][
                                    0]) + end_span + " "
                            text_latin += span + html.escape(
                                self.frameFather.quran[num_pos_word][
                                    0]) + end_span + " "
                            text_arab_save += "((" + translit_to_arab(
                                self.frameFather.quran[num_pos_word][0]) + ")) "
                            text_latin_save += "((" + \
                                               self.frameFather.quran[
                                                   num_pos_word][
                                                   0] + ")) "
                        else:
                            text_arab += translit_to_arab(
                                self.frameFather.quran[num_pos_word][0]) + " "
                            text_latin += html.escape(
                                self.frameFather.quran[num_pos_word][0]) + " "
                            text_arab_save += translit_to_arab(
                                self.frameFather.quran[num_pos_word][0]) + " "
                            text_latin_save += \
                                self.frameFather.quran[num_pos_word][0] + " "
                    item = QtWidgets.QTextEdit()
                    item.setReadOnly(True)
                    item.setText(text_arab)
                    self.frameFather.tableWidget.setCellWidget(i * 2, 3, item)
                    item = QtWidgets.QTextEdit()
                    item.setReadOnly(True)
                    item.insertHtml(
                        "<html><body><p>" + text_latin + "</p></body></html>")
                    self.frameFather.tableWidget.setCellWidget(i * 2 + 1, 3,
                                                               item)
                    self.frameFather.text_save += "%14s | %13s | %6s | %s\n%15s|%15s|%8s| %s\n" % (
                        translit_to_latin(self.frameFather.sourats_names[
                                            int(key[:3]) - ind_first_sourat]),
                        str(int(key[:3])),
                        str(int(key[4:])),
                        text_arab_save,
                        '', '', '', text_latin_save
                    )
                    i += 1
                item = QtWidgets.QTextEdit()
                item.setReadOnly(True)
                item.setText(
                    'Concordancer\nSearch word : %s\nSearch type : %s\n'
                    'Number of Words before and after word found : %d\n'
                    'Verse number found : %d verset(s)\n'
                    'Word number found : %d word(s)\n'
                    "Precision : %f\n"
                    "Recall : %f\n"
                    "F-Score : %f\n\n" % (
                        requete, self.cbTypeSearch.currentText(),
                        self.cbNbrWords.currentIndex(),
                        len(list_results),
                        sum([len(liste[0]) for liste in list_results.values()]),
                        p, r, f_score))
                self.frameFather.tableWidget.setCellWidget(i * 2, 0, item)
                self.frameFather.tableWidget.setSpan(i * 2, 0, 1, 4)
                self.frameFather.tableWidget.resizeColumnToContents(3)
                self.frameFather.tableWidget.resizeRowToContents(i * 2)
                self.frameFather.label.setText(
                    'Operation completed in %.2f seconds' % (endt - startt))
                self.frameFather.pbSave.setEnabled(True)
                self.frameFather.progressBar.setRange(0, 100)
                self.frameFather.progressBar.setValue(100)
                self.MainWindow.setEnabled(True)
                self.frameFather.mainWindow.setEnabled(True)
                self.MainWindow.close()

    def __init__(self, arg):
        super(ConcordancerFrame, self).__init__()
        self.frameFather = arg

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(356, 179)
        MainWindow.setMinimumSize(QtCore.QSize(356, 179))
        MainWindow.setMaximumSize(QtCore.QSize(356, 179))
        self.MainWindow = MainWindow
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setGeometry(QtCore.QRect(40, 140, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.buttonBox.setFont(font)
        self.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gbTypeSearch = QtWidgets.QGroupBox(self.centralwidget)
        self.gbTypeSearch.setGeometry(QtCore.QRect(10, 80, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.gbTypeSearch.setFont(font)
        self.gbTypeSearch.setStyleSheet("QGroupBox {\n"
                                        "    border: 2px solid black;\n"
                                        "    border-radius: 9px;\n"
                                        "    margin-top: 0.5em;\n"
                                        "}\n"
                                        "QGroupBox::title {\n"
                                        "    subcontrol-origin: margin;\n"
                                        "    left: 10px;\n"
                                        "    padding: -2 3px 0 3px;\n"
                                        "}")
        self.gbTypeSearch.setObjectName("gbTypeSearch")
        self.cbTypeSearch = QtWidgets.QComboBox(self.gbTypeSearch)
        self.cbTypeSearch.setGeometry(QtCore.QRect(10, 20, 141, 22))
        self.cbTypeSearch.setObjectName("cbTypeSearch")
        self.cbTypeSearch.addItem("")
        self.cbTypeSearch.addItem("")
        self.cbTypeSearch.addItem("")
        self.gbNbrWords = QtWidgets.QGroupBox(self.centralwidget)
        self.gbNbrWords.setGeometry(QtCore.QRect(180, 80, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.gbNbrWords.setFont(font)
        self.gbNbrWords.setStyleSheet("QGroupBox {\n"
                                      "    border: 2px solid black;\n"
                                      "    border-radius: 9px;\n"
                                      "    margin-top: 0.5em;\n"
                                      "}\n"
                                      "QGroupBox::title {\n"
                                      "    subcontrol-origin: margin;\n"
                                      "    left: 10px;\n"
                                      "    padding: -2 3px 0 3px;\n"
                                      "}")
        self.gbNbrWords.setObjectName("gbNbrWords")
        self.cbNbrWords = QtWidgets.QComboBox(self.gbNbrWords)
        self.cbNbrWords.setGeometry(QtCore.QRect(10, 20, 141, 22))
        self.cbNbrWords.setObjectName("cbNbrWords")
        self.gbWordSearch = QtWidgets.QGroupBox(self.centralwidget)
        self.gbWordSearch.setGeometry(QtCore.QRect(10, 10, 331, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.gbWordSearch.setFont(font)
        self.gbWordSearch.setStyleSheet("QGroupBox {\n"
                                        "    border: 2px solid black;\n"
                                        "    border-radius: 9px;\n"
                                        "    margin-top: 0.5em;\n"
                                        "}\n"
                                        "QGroupBox::title {\n"
                                        "    subcontrol-origin: margin;\n"
                                        "    left: 10px;\n"
                                        "    padding: -2 3px 0 3px;\n"
                                        "}")
        self.gbWordSearch.setObjectName("gbWordSearch")
        self.textEdit = QtWidgets.QTextEdit(self.gbWordSearch)
        self.textEdit.setGeometry(QtCore.QRect(10, 20, 311, 31))
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)

        for i in range(101):
            self.cbNbrWords.addItem(str(i))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.buttonBox.rejected.connect(lambda: self.cancel())
        self.buttonBox.accepted.connect(lambda: self.generate())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Concordance"))
        self.gbTypeSearch.setTitle(
            _translate("MainWindow", "Type of research"))
        self.cbTypeSearch.setItemText(0, _translate("MainWindow", "Lemme"))
        self.cbTypeSearch.setItemText(1, _translate("MainWindow", "Root"))
        self.cbTypeSearch.setItemText(2, _translate("MainWindow",
                                                    "Lemme and Root"))
        self.gbNbrWords.setTitle(_translate("MainWindow", "Number of words"))
        self.gbWordSearch.setTitle(_translate("MainWindow", "Searched word"))
