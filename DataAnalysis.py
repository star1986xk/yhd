import sys
from UI.Ui_mainWin import Ui_Form
from PyQt5.QtWidgets import QDialog, QCheckBox, QListWidgetItem, QWidget, QVBoxLayout, QApplication
from db_class import db_class
from PyQt5.QtCore import QSize,pyqtSignal
from settings import *

class DataAnalysis(Ui_Form, QWidget):
    def __init__(self, parent=None):
        super(DataAnalysis, self).__init__(parent)
        self.setupUi(self)
        self.retranslateUi(self)

        self.load()

    def load(self):
        self.check_list = []
        self.listWidget.clear()
        for k,v in class1_dict.items():
            widget = QWidget()
            Layout = QVBoxLayout()
            check = QCheckBox(k, self)
            self.check_list.append(check)
            Layout.addWidget(check)
            widget.setLayout(Layout)
            item = QListWidgetItem()
            item.setSizeHint(QSize(80, 40))
            self.listWidget.addItem(item)
            self.listWidget.setItemWidget(item, widget)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = DataAnalysis()
    win.show()
    sys.exit(app.exec_())