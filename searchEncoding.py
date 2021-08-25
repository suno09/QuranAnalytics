from collections import defaultdict
from PyQt5 import QtWidgets
from transliteration import translit_to_arab, translit_to_latin
import re
import matplotlib

matplotlib.use('Qt5Agg')

from matplotlib.backends.backend_qt5agg import \
    FigureCanvasQTAgg as FigureCanvas, \
    NavigationToolbar2QT as NavigationToolbar
from time import time
from showdialog import showdialog


def get_versets_by_encoding(encoding: str, quran: dict, ahkaam: dict,
                            frame_father=None):
    """
    get the lists of versets in Quran that contains encoding ahkaam search
    :param encoding: string of digits
    :param quran: quran index of application
    :param ahkaam: ahkaam index of Quran
    :param frame_father: the main window
    :return None
    """
    startt = time()
    list_versets_by_encoding = defaultdict(
        lambda: defaultdict(lambda: [list, str]))
    count_versets = 0
    count_results = 0
    for num_sourat in ahkaam.keys():
        QtWidgets.QApplication.processEvents()
        for i in range(len(ahkaam[num_sourat])):
            QtWidgets.QApplication.processEvents()
            # if encoding exists in verset encoding
            if encoding in ahkaam[num_sourat][i]:
                count_versets += 1
                verset_context = ' '.join(
                    [quran[key][0] for key in sorted(quran.keys())
                     if key.startswith(
                        num_sourat + ':' + "{0:0>3}".format(i + 1))])
                # add verset in result
                list_versets_by_encoding[num_sourat][
                    "{0:0>3}".format(i + 1)] = [
                    [m.start() for m in
                     re.finditer(encoding, ahkaam[num_sourat][i])],
                    verset_context]
                count_results += len(list_versets_by_encoding[num_sourat][
                                         "{0:0>3}".format(i + 1)][0])

    if frame_father and list_versets_by_encoding:
        frame_father.textSave2 = 'Search Encoding\nCoding searched : %s\n' \
                                 'Verse number found : %d verset(s)\n' \
                                 'Coding number found : %d encodings(s)\n\n' % (
                                     encoding, count_versets, count_results)
        frame_father.textSave2 += '     Sourat    | Sourat Number | Verset | Context' \
                                  '\n------------------------------------------------\n'
        import matplotlib.pyplot as plt
        frame_father.listResult2 = list_versets_by_encoding
        frame_father.tableWidget.setStyleSheet("")
        frame_father.tableWidget.setRowCount(0)
        frame_father.tableWidget.setColumnCount(4)
        frame_father.tableWidget.setRowCount(count_versets * 4 + 1)
        frame_father.tableWidget.setColumnWidth(0, 60)
        frame_father.tableWidget.setColumnWidth(1, 60)
        frame_father.tableWidget.setColumnWidth(2, 60)
        frame_father.tableWidget.horizontalHeader().setStretchLastSection(True)
        frame_father.tableWidget.setHorizontalHeaderLabels(
            ['Sourat', 'Sourat\nNumber', 'Verset',
             'Histogram and Context\nEncoding = ' + encoding])
        ind = 0
        ind_first_sourat = int(sorted(ahkaam.keys())[0])
        for num_sourat in sorted(list_versets_by_encoding.keys()):
            QtWidgets.QApplication.processEvents()
            for numVerset in sorted(list_versets_by_encoding[num_sourat]):
                QtWidgets.QApplication.processEvents()
                fig = plt.figure()
                list_encoding = []
                for e in frame_father.ahkaam[num_sourat][int(numVerset) - 1]:
                    QtWidgets.QApplication.processEvents()
                    list_encoding.append(int(e))
                l = []
                for key in sorted(frame_father.quran.keys()):
                    QtWidgets.QApplication.processEvents()
                    if key.startswith(num_sourat + ':' + numVerset):
                        l.append(frame_father.quran[key][0])
                str_verset = ' '.join(l)
                axe = fig.add_subplot(1, 1, 1)
                list_encoding_bars = axe.bar(range(len(list_encoding)),
                                             list_encoding, 1, color='green')
                first_ind = list_versets_by_encoding[num_sourat][numVerset][0]
                for i in first_ind:
                    QtWidgets.QApplication.processEvents()
                    for j in range(i, i + len(encoding)):
                        QtWidgets.QApplication.processEvents()
                        list_encoding_bars[j].set_color('b')
                        list_encoding_bars[j].set_edgecolor('black')
                axe.set_xlabel('')
                axe.set_ylabel('Encoding')
                plt.xlim([0, len(list_encoding)])
                plt.ylim([0, 6])
                plt.gca().axes.get_xaxis().set_visible(False)
                # affichage dans tableau
                item = QtWidgets.QTableWidgetItem()
                item.setText(frame_father.sourats_names[
                                 int(num_sourat) - ind_first_sourat])
                frame_father.tableWidget.setItem(ind * 4, 0, item)
                frame_father.tableWidget.setSpan(ind * 4, 0, 4, 1)
                item = QtWidgets.QTableWidgetItem()
                item.setText(str(num_sourat))
                frame_father.tableWidget.setItem(ind * 4, 1, item)
                frame_father.tableWidget.setSpan(ind * 4, 1, 4, 1)
                item = QtWidgets.QTableWidgetItem()
                item.setText(str(int(numVerset)))
                frame_father.tableWidget.setItem(ind * 4, 2, item)
                frame_father.tableWidget.setSpan(ind * 4, 2, 4, 1)
                frame_father.canvas = FigureCanvas(fig)
                frame_father.canvas.draw()
                frame_father.toolbar = NavigationToolbar(frame_father.canvas,
                                                         frame_father.mainWindow,
                                                         coordinates=True)
                frame_father.tableWidget.setCellWidget(ind * 4, 3,
                                                       frame_father.toolbar)
                frame_father.tableWidget.setCellWidget(ind * 4 + 1, 3,
                                                       frame_father.canvas)
                frame_father.tableWidget.setRowHeight(ind * 4 + 1, 150)
                item = QtWidgets.QTextEdit()
                item.setReadOnly(True)
                item.setText(translit_to_arab(str_verset))
                frame_father.tableWidget.setCellWidget(ind * 4 + 2, 3, item)
                item = QtWidgets.QTextEdit()
                item.setReadOnly(True)
                item.setText(str_verset)
                frame_father.tableWidget.setCellWidget(ind * 4 + 3, 3, item)
                frame_father.text_save.append(fig)
                frame_father.textSave2 += "%14s | %13s | %6s | %s\n%15s|%15s|%8s| %s\n" % (
                    translit_to_latin(frame_father.sourats_names[
                                          int(num_sourat) - ind_first_sourat]),
                    num_sourat,
                    numVerset,
                    translit_to_arab(str_verset),
                    '', '', '', str_verset
                )
                ind += 1
        item = QtWidgets.QTextEdit()
        item.setReadOnly(True)
        item.setText('Search Encoding\nCoding searched : %s\n'
                     'Verse number found : %d verset(s)\n'
                     'Coding number found : %d encodings(s)\n\n' %
                     (encoding, count_versets, count_results))
        frame_father.tableWidget.setCellWidget(ind * 4, 0, item)
        frame_father.tableWidget.setSpan(ind * 4, 0, 1, 4)
        frame_father.tableWidget.resizeColumnToContents(3)
        frame_father.tableWidget.resizeRowToContents(ind * 4)
        frame_father.label.setText(
            'Operation completed in %.2f seconds' % (time() - startt))
        frame_father.progressBar.setRange(0, 100)
        frame_father.progressBar.setValue(100)
        frame_father.pbSave.setEnabled(True)
    else:
        showdialog(QtWidgets.QMessageBox.Critical, 'Error',
                   "No result found !")
        frame_father.progressBar.setRange(0, 100)
        frame_father.progressBar.setValue(0)
        frame_father.label.setText("")
