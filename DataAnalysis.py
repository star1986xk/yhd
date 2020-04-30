import sys
import time
from UI.Ui_mainWin import Ui_Form
from PyQt5.QtWidgets import QTableWidgetItem, QCheckBox, QListWidgetItem, QWidget, QVBoxLayout, QApplication, \
    QHeaderView
from db_class import db_class
from PyQt5.QtCore import QSize
from settings import *
from search_class import search_class
from MyFigure import MyFigure


class DataAnalysis(Ui_Form, QWidget):
    def __init__(self, parent=None):
        '''
        程序初始化
        :param parent:
        '''
        super(DataAnalysis, self).__init__(parent)
        self.setupUi(self)
        self.retranslateUi(self)

        headerView = self.tableWidget.horizontalHeader()
        headerView.setSectionResizeMode(QHeaderView.Stretch)

        self.pushButton_run.clicked.connect(self.run)
        self.tabWidget.currentChanged.connect(self.tabChange)
        self.pushButton_del.clicked.connect(self.del_data)
        self.pushButton_sel.clicked.connect(self.sel_data)
        self.pushButton_als.clicked.connect(self.analysis)
        self.load()

        self.db = db_class()

    def load(self):
        '''
        载入分类勾选项
        :return:
        '''
        self.class_check_list = []
        self.listWidget.clear()
        for k, v in class1_dict.items():
            widget = QWidget()
            Layout = QVBoxLayout()
            check = QCheckBox(k, self)
            self.class_check_list.append(check)
            Layout.addWidget(check)
            widget.setLayout(Layout)
            item = QListWidgetItem()
            item.setSizeHint(QSize(80, 40))
            self.listWidget.addItem(item)
            self.listWidget.setItemWidget(item, widget)

    def run(self):
        '''
        爬虫开始
        :return:
        '''
        class_list = [class1_dict[c.text()] for c in self.class_check_list if c.isChecked()]
        page_count = self.spinBox_page.text()
        thread_count = self.spinBox_thread.text()
        if len(class_list) > 0:
            self.search_obj = search_class(class_list, page_count, thread_count)
            self.search_obj.sig_one_end.connect(self.one_end)
            self.search_obj.sig_end.connect(self.end)
            self.search_obj.start()

            self.spinBox_page.setDisabled(True)
            self.spinBox_thread.setDisabled(True)
            self.pushButton_run.setDisabled(True)
            self.textBrowser.setText('运行程序! ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

    def one_end(self, text):
        '''
        爬虫完成一个线程
        :param text: 文本信息写入日志
        :return:
        '''
        self.textBrowser.append(text)

    def end(self, text):
        '''
        爬虫全部完成
        :param text: 文本信息写入日志
        :return:
        '''
        self.textBrowser.append(text)
        self.spinBox_page.setDisabled(False)
        self.spinBox_thread.setDisabled(False)
        self.pushButton_run.setDisabled(False)

    def tabChange(self, index):
        '''
        tab改变时，载入勾选项
        :param index:
        :return:
        '''
        if index == 1:
            self.db.open()
            uid_list = self.db.select_uid(table_name)
            self.db_check_list = []
            self.listWidget_2.clear()
            for li in uid_list:
                widget = QWidget()
                Layout = QVBoxLayout()
                check = QCheckBox(li[0], self)
                self.db_check_list.append(check)
                Layout.addWidget(check)
                widget.setLayout(Layout)
                item = QListWidgetItem()
                item.setSizeHint(QSize(80, 40))
                self.listWidget_2.addItem(item)
                self.listWidget_2.setItemWidget(item, widget)
        elif index == 2:
            self.db.open()
            sel_list = self.db.select_uid(table_name)
            self.al_check_list = []
            self.listWidget_3.clear()
            for li in sel_list:
                widget = QWidget()
                Layout = QVBoxLayout()
                check = QCheckBox(li[0], self)
                self.al_check_list.append(check)
                Layout.addWidget(check)
                widget.setLayout(Layout)
                item = QListWidgetItem()
                item.setSizeHint(QSize(80, 40))
                self.listWidget_3.addItem(item)
                self.listWidget_3.setItemWidget(item, widget)

    def del_data(self):
        '''
        删除勾选数据
        :return:
        '''
        uid_list = [c.text() for c in self.db_check_list if c.isChecked()]
        self.db.delete_many(table_name, [{'uid': uid} for uid in uid_list])
        self.tabChange(1)
        self.tableWidget.setRowCount(0)

    def sel_data(self):
        '''
        根据勾选项查询数据，并把数据写入表
        :return:
        '''
        datas = []
        uid_list = [c.text() for c in self.db_check_list if c.isChecked()]
        for uid in uid_list:
            datas += list(self.db.select_condition(table_name, {'uid': uid}))
        if datas:
            self.load_table(datas)

    def load_table(self, items):
        '''
        数据写入表
        :param items:数据集合
        :return:
        '''
        try:
            self.tableWidget.setRowCount(0)
            for n, item in enumerate(items):
                print(items)
                self.tableWidget.setRowCount(n + 1)
                self.tableWidget.setItem(n, 0, QTableWidgetItem(str(item[1])))
                self.tableWidget.setItem(n, 1, QTableWidgetItem(str(item[2])))
                self.tableWidget.setItem(n, 2, QTableWidgetItem(str(item[3])))
                self.tableWidget.setItem(n, 3, QTableWidgetItem(str(item[4])))
                self.tableWidget.setItem(n, 4, QTableWidgetItem(str(item[7])))
                self.tableWidget.setItem(n, 5, QTableWidgetItem(str(item[8])))
                self.tableWidget.setItem(n, 6, QTableWidgetItem(str(item[10])))
        except Exception as e:
            print(e)

    def analysis(self):
        '''
        数据分析
        :return:
        '''
        al_list = [c.text() for c in self.al_check_list if c.isChecked()]
        if al_list:
            self.db.open()
            class_sales_sum = self.db.select_group_sum(table_name, al_list, 'class3', 'sales')
            class_money_avg = self.db.select_group_avg(table_name, al_list, 'class3', 'money')
            class_goodCount_avg = self.db.select_group_avg(table_name, al_list, 'class3', 'goodCount')
            class_generalCount_avg = self.db.select_group_avg(table_name, al_list, 'class3', 'generalCount')
            class_poorCount_avg = self.db.select_group_avg(table_name, al_list, 'class3', 'poorCount')

            shop_sales_sum = self.db.select_group_top10_sum(table_name, al_list, 'shop', 'sales')
            shop_money_avg = self.db.select_group_top10_avg(table_name, al_list, 'shop', 'money')
            shop_goodCount_avg = self.db.select_group_top10_avg(table_name, al_list, 'shop', 'goodCount')
            shop_generalCount_avg = self.db.select_group_top10_avg(table_name, al_list, 'shop', 'generalCount')
            shop_poorCount_avg = self.db.select_group_top10_avg(table_name, al_list, 'shop', 'poorCount')

            sales_money = self.db.select_two_fields(table_name, al_list, 'sales', 'money')
            goodCount_money = self.db.select_two_fields(table_name, al_list, 'goodCount', 'money')
            generalCount_money = self.db.select_two_fields(table_name, al_list, 'generalCount', 'money')
            poorCount_money = self.db.select_two_fields(table_name, al_list, 'poorCount', 'money')
            self.db.close()

            # 分类分析
            x = [i[1] for i in class_sales_sum]
            y = [i[0] for i in class_sales_sum]
            self.MyFig = MyFigure()
            self.MyFig.axes.pie(y, labels=x, autopct='%1.1f%%')
            self.MyFig.axes.set_title("分类销量占比")
            self.MyFig.axes.set_xticklabels(x, fontsize=8, rotation=20)
            for i in range(self.verticalLayout_2.count()):
                self.verticalLayout_2.itemAt(i).widget().deleteLater()
            self.verticalLayout_2.addWidget(self.MyFig)

            x = [i[1] for i in class_sales_sum]
            y = [i[0] for i in class_sales_sum]
            self.MyFig = MyFigure()
            self.MyFig.axes.bar(x, y)
            self.MyFig.axes.set_title("分类销量数")
            self.MyFig.axes.set_xticklabels(x, fontsize=8, rotation=20)
            for i in range(self.verticalLayout_6.count()):
                self.verticalLayout_6.itemAt(i).widget().deleteLater()
            self.verticalLayout_6.addWidget(self.MyFig)

            self.MyFig = MyFigure()
            x1 = [i[1] for i in class_money_avg]
            y1 = [i[0] for i in class_money_avg]
            self.MyFig.axes.plot(x1, y1)
            self.MyFig.axes.set_title("分类均价")
            self.MyFig.axes.set_xticklabels(x1, fontsize=8, rotation=20)
            for i in range(self.verticalLayout_7.count()):
                self.verticalLayout_7.itemAt(i).widget().deleteLater()
            self.verticalLayout_7.addWidget(self.MyFig)

            self.MyFig = MyFigure()
            x2 = [i[1] for i in class_goodCount_avg]
            y2 = [i[0] for i in class_goodCount_avg]
            x3 = [i[1] for i in class_generalCount_avg]
            y3 = [i[0] for i in class_generalCount_avg]
            x4 = [i[1] for i in class_poorCount_avg]
            y4 = [i[0] for i in class_poorCount_avg]
            self.MyFig.axes.plot(x2, y2, label='好评数')
            self.MyFig.axes.plot(x3, y3, label='中评数')
            self.MyFig.axes.plot(x4, y4, label='差评数')
            self.MyFig.axes.legend()
            self.MyFig.axes.set_title("分类评价")
            self.MyFig.axes.set_xticklabels(x2, fontsize=8, rotation=20)
            for i in range(self.verticalLayout_8.count()):
                self.verticalLayout_8.itemAt(i).widget().deleteLater()
            self.verticalLayout_8.addWidget(self.MyFig)

            # 店铺分析
            x5 = [i[1] for i in shop_sales_sum]
            y5 = [i[0] for i in shop_sales_sum]
            self.MyFig = MyFigure()
            self.MyFig.axes.pie(y5, labels=x5, autopct='%1.1f%%')
            self.MyFig.axes.set_title("TOP10店铺销量占比")
            self.MyFig.axes.set_xticklabels(x5, fontsize=8, rotation=10)
            for i in range(self.verticalLayout_9.count()):
                self.verticalLayout_9.itemAt(i).widget().deleteLater()
            self.verticalLayout_9.addWidget(self.MyFig)

            x6 = [i[1] for i in shop_sales_sum]
            y6 = [i[0] for i in shop_sales_sum]
            self.MyFig = MyFigure()
            self.MyFig.axes.bar(x6, y6)
            self.MyFig.axes.set_title("TOP10店铺销量数")
            self.MyFig.axes.set_xticklabels(x6, fontsize=8, rotation=20)
            for i in range(self.verticalLayout_10.count()):
                self.verticalLayout_10.itemAt(i).widget().deleteLater()
            self.verticalLayout_10.addWidget(self.MyFig)

            self.MyFig = MyFigure()
            x7 = [i[1] for i in shop_money_avg]
            y7 = [i[0] for i in shop_money_avg]
            self.MyFig.axes.plot(x7, y7)
            self.MyFig.axes.set_title("TOP10店铺均价")
            self.MyFig.axes.set_xticklabels(x7, fontsize=8, rotation=20)
            for i in range(self.verticalLayout_11.count()):
                self.verticalLayout_11.itemAt(i).widget().deleteLater()
            self.verticalLayout_11.addWidget(self.MyFig)

            self.MyFig = MyFigure()
            x8 = [i[1] for i in shop_goodCount_avg]
            y8 = [i[0] for i in shop_goodCount_avg]
            x9 = [i[1] for i in shop_generalCount_avg]
            y9 = [i[0] for i in shop_generalCount_avg]
            x10 = [i[1] for i in shop_poorCount_avg]
            y10 = [i[0] for i in shop_poorCount_avg]
            self.MyFig.axes.plot(x8, y8, label='好评数')
            self.MyFig.axes.plot(x9, y9, label='中评数')
            self.MyFig.axes.plot(x10, y10, label='差评数')
            self.MyFig.axes.legend()
            self.MyFig.axes.set_title("TOP10店铺评价")
            self.MyFig.axes.set_xticklabels(x8, fontsize=8, rotation=20)
            for i in range(self.verticalLayout_12.count()):
                self.verticalLayout_12.itemAt(i).widget().deleteLater()
            self.verticalLayout_12.addWidget(self.MyFig)

            # 综合分析
            self.MyFig = MyFigure()
            x11 = [i[1] for i in sales_money]
            y11 = [i[0] for i in sales_money]
            self.MyFig.axes.scatter(x11, y11)
            self.MyFig.axes.set_title("销量及价格")
            self.MyFig.axes.set_ylabel('销量')
            self.MyFig.axes.set_xlabel('价格')
            for i in range(self.verticalLayout_13.count()):
                self.verticalLayout_13.itemAt(i).widget().deleteLater()
            self.verticalLayout_13.addWidget(self.MyFig)

            self.MyFig = MyFigure()
            x12 = [i[1] for i in goodCount_money]
            y12 = [i[0] for i in goodCount_money]
            self.MyFig.axes.scatter(x12, y12)
            self.MyFig.axes.set_title("好评及价格")
            self.MyFig.axes.set_ylabel('好评数')
            self.MyFig.axes.set_xlabel('价格')
            for i in range(self.verticalLayout_14.count()):
                self.verticalLayout_14.itemAt(i).widget().deleteLater()
            self.verticalLayout_14.addWidget(self.MyFig)

            self.MyFig = MyFigure()
            x13 = [i[1] for i in generalCount_money]
            y13 = [i[0] for i in generalCount_money]
            self.MyFig.axes.scatter(x13, y13)
            self.MyFig.axes.set_title("中评及价格")
            self.MyFig.axes.set_ylabel('中评数')
            self.MyFig.axes.set_xlabel('价格')
            for i in range(self.verticalLayout_15.count()):
                self.verticalLayout_15.itemAt(i).widget().deleteLater()
            self.verticalLayout_15.addWidget(self.MyFig)

            self.MyFig = MyFigure()
            x14 = [i[1] for i in poorCount_money]
            y14 = [i[0] for i in poorCount_money]
            self.MyFig.axes.scatter(x14, y14)
            self.MyFig.axes.set_title("差评及价格")
            self.MyFig.axes.set_ylabel('差评数')
            self.MyFig.axes.set_xlabel('价格')
            for i in range(self.verticalLayout_16.count()):
                self.verticalLayout_16.itemAt(i).widget().deleteLater()
            self.verticalLayout_16.addWidget(self.MyFig)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = DataAnalysis()
    win.show()
    sys.exit(app.exec_())
