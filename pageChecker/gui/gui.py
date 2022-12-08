"""
TODO:
    try execpt - working
    add adapter for data
"""

import ctypes
import re
import sys
sys.path.append("gui")
import webbrowser

from PyQt5 import QtWidgets, uic, QtCore, QtGui

from datav import Mock
from datav import mock_data_list as data




class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, db, style):
        super(MainWindow, self).__init__()
        uic.loadUi('gui/win.ui', self)
        self.db = db
        self.style = style
        self.create_layout()
        self.format_dynamic_text()
        self.setWindowIcon(QtGui.QIcon('gui/logo.png'))

        self.setWindowTitle("PageChecker")

        self.show()

    def resizeEvent(self, event: QtGui.QResizeEvent) -> None:
        w = event.size().width() - 300
        h = event.size().height() - 110

        self.widget_items_of_site.setGeometry(QtCore.QRect(270, 50, w, h))
        self.widget_list_of_sites.setGeometry(QtCore.QRect(30, 50, 231, h + 3))

    def create_layout(self):

        self.widget_list_of_sites: QtWidgets.QListWidget = self.findChild(QtWidgets.QListWidget, 'widget_list_of_sites')
        self.widget_list_of_sites.itemClicked.connect(self.format_widget_list_of_sites)

        self.widget_items_of_site = self.findChild(QtWidgets.QTreeWidget, 'widget_items_of_site')
        self.widget_items_of_site.doubleClicked.connect(self.webbrowser_to_open)

        self.button_add_site = self.findChild(QtWidgets.QPushButton, 'button_add_site')
        self.button_add_site.clicked.connect(self.add_site)

        self.button_remove_site = self.findChild(QtWidgets.QPushButton, 'button_remove_site')
        self.button_remove_site.clicked.connect(self.remove_site)

        self.button_font_plus = self.findChild(QtWidgets.QPushButton, 'button_font_plus')
        self.button_font_plus.clicked.connect(self.format_style_font_plus)

        self.button_font_minus = self.findChild(QtWidgets.QPushButton, 'button_font_minus')
        self.button_font_minus.clicked.connect(self.format_style_font_minus)

        self.button_update = self.findChild(QtWidgets.QPushButton, 'button_update')
        self.button_update.clicked.connect(self.update_all_sites)

        self.button_color_gray = self.findChild(QtWidgets.QPushButton, 'button_color_gray')
        self.button_color_gray.clicked.connect(self.format_style_theme_grey)

        self.button_color_white = self.findChild(QtWidgets.QPushButton, 'button_color_white')
        self.button_color_white.clicked.connect(self.format_style_theme_white)


    def add_site(self):
        s = DialogChoice(self)
        s.exec_()

    def remove_site(self):
        a = self.widget_list_of_sites.currentRow()
        self.widget_list_of_sites.takeItem(a)

    def update_all_sites(self):
        pass

    def format_style_theme_white(self):

        self.style = self.style.replace("color: #ffffff;", "color: #000000;")
        self.style = self.style.replace("color: #FFFFFF;", "color: #000000;")
        self.style = self.style.replace("background: #262D37;", "background: #FFFFFF;")

        self.setStyleSheet(self.style)

    def format_style_theme_grey(self):
        self.style = self.style.replace("color: #000000;", "color: #ffffff;")
        self.style = self.style.replace("color: #000000;", "color: #FFFFFF;")
        self.style = self.style.replace("background: #FFFFFF;", "background: #262D37;")

        self.setStyleSheet(self.style)

    def format_dynamic_text(self):
        self.widget_list_of_sites.clear()

        _translate = QtCore.QCoreApplication.translate

        for site in self.db:
            item = QtWidgets.QListWidgetItem()
            item.setText(_translate("MainWindow", f"{site.name}"))
            # item.setSizeHint(QSize(10, 20))
            # item.setFont()
            self.widget_list_of_sites.addItem(item)

    def format_widget_list_of_sites(self, item):

        self.widget_items_of_site.clear()

        _translate = QtCore.QCoreApplication.translate
        __sortingEnabled = self.widget_items_of_site.isSortingEnabled()
        self.widget_items_of_site.setSortingEnabled(False)
        # self.widget_items_of_site.headerItem().setText(0, _translate("MainWindow", "title"))
        # self.widget_items_of_site.headerItem().setColor(QtGui.QColor(93, 93, 93))
        # self.widget_items_of_site.headerItem().setText(1, _translate("MainWindow", "url"))
        # self.widget_items_of_site.headerItem().setText(2, _translate("MainWindow", "date"))
        # self.widget_items_of_site.headerItem().setText(3, _translate("MainWindow", "content"))

        for site in self.db:
            if site.name == item.text():
                for index, post in enumerate(site.data):
                    item_0 = QtWidgets.QTreeWidgetItem(self.widget_items_of_site)

                    self.widget_items_of_site.topLevelItem(index).setText(0, _translate("MainWindow", post.url))
                    self.widget_items_of_site.topLevelItem(index).setText(1, _translate("MainWindow", post.date))
                    self.widget_items_of_site.topLevelItem(index).setText(2, _translate("MainWindow", post.title))
                    self.widget_items_of_site.topLevelItem(index).setText(3, _translate("MainWindow", post.content))

        self.widget_items_of_site.setSortingEnabled(__sortingEnabled)

    def webbrowser_to_open(self, site):
        s = self.widget_items_of_site.itemFromIndex(site).text(0)
        webbrowser.open(s)

    def format_style_font_plus(self):
        matches = re.findall("(font-size: {0,3})(\d{1,4})", self.style)

        for match in matches:
            base = match[0] + match[1]
            size_add = int(match[1]) + 1
            res = match[0] + str(size_add)

            self.style = self.style.replace(base, res)

        self.setStyleSheet(self.style)

    def format_style_font_minus(self):
        matches = re.findall("(font-size: {0,3})(\d{1,4})", self.style)

        for match in matches:
            base = match[0] + match[1]
            size_add = int(match[1]) - 1
            res = match[0] + str(size_add)

            self.style = self.style.replace(base, res)

        self.setStyleSheet(self.style)


class DialogChoice(QtWidgets.QDialog):
    def __init__(self, main_windows):
        self.main_windows = main_windows

        super(DialogChoice, self).__init__()
        uic.loadUi('gui/dialog.ui', self)

        self.setWindowIcon(QtGui.QIcon('gui/logo.png'))
        self.setWindowTitle("Dialog")

        self.create_layout()

        self.show()

    def create_layout(self):
        self.input_name = self.findChild(QtWidgets.QLineEdit, 'input_name')
        self.input_url = self.findChild(QtWidgets.QLineEdit, 'input_url')
        self.input_find = self.findChild(QtWidgets.QLineEdit, 'input_find')

        self.button_choice_bool = self.findChild(QtWidgets.QDialogButtonBox, 'button_choice_bool')
        self.button_choice_bool.accepted.connect(self.accept_data)
        self.button_choice_bool.rejected.connect(self.rejected_data)

    def accept_data(self):
        self.main_windows.db.append(Mock(self.input_name.text()))
        self.main_windows.format_dynamic_text()

    def rejected_data(self):
        pass


def create_ui(db):
    myappid = 'PageChecker'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    with open("gui/style.css") as file:
        style = file.read()

    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(style)
    window = MainWindow(db, style)
    app.exec_()


def main():
    create_ui(data)


if __name__ == '__main__':
    main()
