from PyQt5 import QtWidgets


def showdialog(type_icon, title, content):
    """
    Show message dialog in the application
    :param type_icon: the type of icon (error, success, ...)
    :param title: the title of dialog
    :param content: the content of dialog
    """
    msg = QtWidgets.QMessageBox()
    msg.setIcon(type_icon)

    msg.setText(content)
    msg.setWindowTitle(title)
    msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
    msg.exec_()
