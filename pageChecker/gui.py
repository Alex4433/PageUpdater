from PyQt5 import QtWidgets, uic, QtCore, QtGui
from PyQt5.QtCore import Qt

import sys





class Ui(QtWidgets.QMainWindow):

    def __init__(self, db):
        super(Ui, self).__init__()
        self.db = db
        uic.loadUi('gui.ui', self)

        self.create_widgets()
        self.format_items()
        self.show()

    def create_widgets(self):
        self.output_ps = self.findChild(QtWidgets.QTextBrowser, 'output_ps')

        self.site_list = self.findChild(QtWidgets.QListWidget, 'site_list')
        self.site_list.itemClicked.connect(self.selected_ls)

        self.setStyleSheet("font-size: 18px;")
        # self.output_ps.setText("test")
        # self.output_ps.setStyleSheet("font-size: 18px;")
        # self.output_ps.setStyleSheet("color: #b57900;")


    def selected_ls(self, item):
        for ds in self.db:
            if ds.name == item.text():

                f = ""

                for d in ds.data:
                    f += f"{d.title} | {d.url}\n"


                self.output_ps.setText(f)

    def format_items(self):
        _translate = QtCore.QCoreApplication.translate

        for ds in self.db:
            item = QtWidgets.QListWidgetItem()
            item.setText(_translate("MainWindow", ds.name))
            self.site_list.addItem(item)

    def format_text_browser(self):
        pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()
