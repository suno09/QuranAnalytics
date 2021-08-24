from transliteration import translit_to_arab, buckWalterSansTashkil
from PyQt5 import QtWidgets
import matplotlib

matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import \
    FigureCanvasQTAgg as FigureCanvas, \
    NavigationToolbar2QT as NavigationToolbar


def plot_histogram(sourat, num_sourat: int, verset_min, verset_max, quran: dict,
                   ahkaam: dict, frame_father):
    """
    Plot histogram of ahkaam encoding (Extend the letter with the sound)
    :param sourat: the sourat name
    :param num_sourat: number of sourat in quran [1..114]
    :param verset_min: the start of verset in sourat
    :param verset_max: the end of verset in sourat
    :param quran: the quran index
    :param ahkaam: dictionary of ahkaam encoding with format
                    {sourat_num: list of verset ahkaam encoding}
    :param frame_father: the main window
    """
    import matplotlib.pyplot as plt
    frame_father.text_save = []
    num_sourat = "{0:0>3}".format(num_sourat)
    frame_father.tableWidget.setStyleSheet("")
    frame_father.tableWidget.setRowCount(0)
    frame_father.tableWidget.setColumnCount(4)
    frame_father.tableWidget.setRowCount((verset_max - verset_min + 1) * 4)
    frame_father.tableWidget.setColumnWidth(0, 60)
    frame_father.tableWidget.setColumnWidth(1, 60)
    frame_father.tableWidget.setColumnWidth(2, 60)
    frame_father.tableWidget.horizontalHeader().setStretchLastSection(True)
    frame_father.tableWidget.setHorizontalHeaderLabels(
        ['Sourat', 'Sourat\nNumber', 'Verset\nnumber',
         'Histogram and Verse Content in Arabic and Latin'])
    for i in range(verset_min, verset_max + 1):
        QtWidgets.QApplication.processEvents()
        ind = i - verset_min
        fig = plt.figure()
        list_encoding = []
        for encode in ahkaam[num_sourat][i - 1]:
            QtWidgets.QApplication.processEvents()
            list_encoding.append(int(encode))
        l = []
        for key in sorted(quran.keys()):
            QtWidgets.QApplication.processEvents()
            if key.startswith(num_sourat + ':' + "{0:0>3}".format(i)):
                l.append(quran[key][0])
        str_verset = ' '.join(l)
        axe = fig.add_subplot(1, 1, 1)
        axe.bar(range(len(list_encoding)), list_encoding, 1, color='green')
        axe.set_xlabel('')
        axe.set_ylabel('Encodage')
        plt.xlim([0, len(list_encoding)])
        plt.ylim([0, 6])
        plt.gca().axes.get_xaxis().set_visible(False)
        # affichage dans tableau
        item = QtWidgets.QTableWidgetItem()
        item.setText(sourat)
        frame_father.tableWidget.setItem(ind * 4, 0, item)
        frame_father.tableWidget.setSpan(ind * 4, 0, 4, 1)
        item = QtWidgets.QTableWidgetItem()
        item.setText(str(num_sourat))
        frame_father.tableWidget.setItem(ind * 4, 1, item)
        frame_father.tableWidget.setSpan(ind * 4, 1, 4, 1)
        item = QtWidgets.QTableWidgetItem()
        item.setText(str(i))
        frame_father.tableWidget.setItem(ind * 4, 2, item)
        frame_father.tableWidget.setSpan(ind * 4, 2, 4, 1)
        frame_father.canvas = FigureCanvas(fig)
        frame_father.canvas.draw()
        frame_father.toolbar = NavigationToolbar(frame_father.canvas,
                                                 frame_father.mainWindow,
                                                 coordinates=True)
        frame_father.tableWidget.setCellWidget(ind * 4, 3, frame_father.toolbar)
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
    frame_father.tableWidget.resizeColumnToContents(3)
