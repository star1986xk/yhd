# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_mainWin.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1053, 727)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/ico/数据.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("QWidget{background-color: #212121;}\n"
"\n"
"QTableWidget{\n"
"color:#DCDCDC;\n"
"background:#444444;\n"
"border:1px solid #242424;\n"
"alternate-background-color:#525252;/*交错颜色*/\n"
"gridline-color:#242424;\n"
"}\n"
"\n"
"/*选中item*/\n"
"QTableWidget::item:selected{\n"
"color:#DCDCDC;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #484848,stop:1 #383838);\n"
"}\n"
"\n"
"/*\n"
"悬浮item*/\n"
"QTableWidget::item:hover{\n"
"background:#5B5B5B;\n"
"}\n"
"/*表头*/\n"
"QHeaderView::section{\n"
"text-align:center;\n"
"background:#5E5E5E;\n"
"padding:3px;\n"
"margin:0px;\n"
"color:#DCDCDC;\n"
"border:1px solid #242424;\n"
"border-left-width:0;\n"
"}\n"
"\n"
"/*表右侧的滑条*/\n"
"QScrollBar:vertical{\n"
"background:#484848;\n"
"padding:0px;\n"
"border-radius:6px;\n"
"max-width:12px;\n"
"}\n"
"\n"
"/*滑块*/\n"
"QScrollBar::handle:vertical{\n"
"background:#CCCCCC;\n"
"}\n"
"/*\n"
"滑块悬浮，按下*/\n"
"QScrollBar::handle:hover:vertical,QScrollBar::handle:pressed:vertical{\n"
"background:#A7A7A7;\n"
"}\n"
"/*\n"
"滑块已经划过的区域*/\n"
"QScrollBar::sub-page:vertical{\n"
"background:444444;\n"
"}\n"
"\n"
"/*\n"
"滑块还没有划过的区域*/\n"
"QScrollBar::add-page:vertical{\n"
"background:5B5B5B;\n"
"}\n"
"\n"
"/*页面下移的按钮*/\n"
"QScrollBar::add-line:vertical{\n"
"background:none;\n"
"}\n"
"/*页面上移的按钮*/\n"
"QScrollBar::sub-line:vertical{\n"
"background:none;\n"
"}\n"
"QGroupBox{\n"
"background-color:rgb(80, 80, 80);color:white;border-radius: 5px;border: 1px solid rgb(255, 170, 0);margin-top: 5px;\n"
"}\n"
"QGroupBox::title{top:-5px;left:10px;}\n"
"QlistWidget{background-color: rgb(68, 68, 68);color:white;}\n"
"QGroupBox QWidget{background-color: rgb(80, 80, 80);color:white;}\n"
"QTextBrowser{background-color: rgb(68, 68, 68);}\n"
"QLabel{color:white;}\n"
"QPushButton{border-radius: 10px;}\n"
"QPushButton:hover{\n"
"color:black;\n"
"background-color: rgb(150, 150, 150);\n"
"}")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tabWidget.setStyleSheet("#tabWidget>QWidget>QWidget{/*tab页*/\n"
"background-color: rgb(80, 80, 80);\n"
"}\n"
"#tabWidget::tab-bar{\n"
"alignment:left;/*tab位置*/\n"
"}\n"
"#tabWidget::pane { /*内容区域*/\n"
"background-color: rgb(80, 80, 80);/*背景色-空隙颜色*/\n"
"\n"
"} \n"
"#tabWidget QTabBar{\n"
"color:white;\n"
"background-color:transparent;\n"
"}\n"
"#tabWidget QTabBar::tab{/*页签*/\n"
"min-height:20px;\n"
"width:120px;\n"
"border-top-left-radius:20px;\n"
"border-bottom-right-radius:20px;\n"
"margin-right:1px;\n"
"margin-bottom:1px;\n"
"background-color:rgb(80, 80, 80);\n"
"}\n"
"#tabWidget QTabBar::tab:hover{\n"
"color:black;\n"
"background-color: rgb(255, 170, 0);\n"
"border-bottom-right-radius:0px;\n"
"}\n"
"#tabWidget QTabBar::tab:selected{\n"
"color:rgb(255, 170, 0);\n"
"border-bottom-right-radius:0px;\n"
"}\n"
"#tabWidget QTabBar::tab:selected:hover{\n"
"color:black;\n"
"}\n"
"#tabWidget QTabBar::tear{/*选项过多时的。。。*/\n"
"imag:;\n"
"}\n"
"#tabWidget QTabBar::scroller{\n"
"width:60px;\n"
"}")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_3.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setMinimumSize(QtCore.QSize(200, 0))
        self.groupBox_2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.listWidget = QtWidgets.QListWidget(self.groupBox_2)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_3.addWidget(self.listWidget)
        self.widget_5 = QtWidgets.QWidget(self.groupBox_2)
        self.widget_5.setMinimumSize(QtCore.QSize(150, 40))
        self.widget_5.setMaximumSize(QtCore.QSize(150, 40))
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_3 = QtWidgets.QLabel(self.widget_5)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3)
        self.spinBox_page = QtWidgets.QSpinBox(self.widget_5)
        self.spinBox_page.setMinimum(1)
        self.spinBox_page.setProperty("value", 1)
        self.spinBox_page.setObjectName("spinBox_page")
        self.horizontalLayout_6.addWidget(self.spinBox_page)
        self.verticalLayout_3.addWidget(self.widget_5, 0, QtCore.Qt.AlignHCenter)
        self.widget_6 = QtWidgets.QWidget(self.groupBox_2)
        self.widget_6.setMinimumSize(QtCore.QSize(150, 40))
        self.widget_6.setMaximumSize(QtCore.QSize(150, 40))
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_4 = QtWidgets.QLabel(self.widget_6)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_7.addWidget(self.label_4)
        self.spinBox_thread = QtWidgets.QSpinBox(self.widget_6)
        self.spinBox_thread.setMinimum(1)
        self.spinBox_thread.setProperty("value", 1)
        self.spinBox_thread.setObjectName("spinBox_thread")
        self.horizontalLayout_7.addWidget(self.spinBox_thread)
        self.verticalLayout_3.addWidget(self.widget_6, 0, QtCore.Qt.AlignHCenter)
        self.pushButton_run = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_run.setMinimumSize(QtCore.QSize(80, 30))
        self.pushButton_run.setMaximumSize(QtCore.QSize(80, 30))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/ico/终极蜘蛛侠.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_run.setIcon(icon1)
        self.pushButton_run.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_run.setObjectName("pushButton_run")
        self.verticalLayout_3.addWidget(self.pushButton_run, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_3.addWidget(self.groupBox_2)
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrowser.setStyleSheet("")
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayout_5.addWidget(self.textBrowser)
        self.horizontalLayout_3.addWidget(self.groupBox)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_3.setMinimumSize(QtCore.QSize(200, 0))
        self.groupBox_3.setMaximumSize(QtCore.QSize(200, 16777215))
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.listWidget_2 = QtWidgets.QListWidget(self.groupBox_3)
        self.listWidget_2.setObjectName("listWidget_2")
        self.verticalLayout_4.addWidget(self.listWidget_2)
        self.pushButton_del = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_del.setMinimumSize(QtCore.QSize(80, 30))
        self.pushButton_del.setMaximumSize(QtCore.QSize(80, 30))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/ico/删除.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_del.setIcon(icon2)
        self.pushButton_del.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_del.setObjectName("pushButton_del")
        self.verticalLayout_4.addWidget(self.pushButton_del, 0, QtCore.Qt.AlignHCenter)
        self.pushButton_sel = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_sel.setMinimumSize(QtCore.QSize(80, 30))
        self.pushButton_sel.setMaximumSize(QtCore.QSize(80, 30))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/newPrefix/ico/3D眼镜.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_sel.setIcon(icon3)
        self.pushButton_sel.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_sel.setObjectName("pushButton_sel")
        self.verticalLayout_4.addWidget(self.pushButton_sel, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox_4)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout.addWidget(self.groupBox_4)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_5.setMinimumSize(QtCore.QSize(200, 0))
        self.groupBox_5.setMaximumSize(QtCore.QSize(200, 16777215))
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.listWidget_3 = QtWidgets.QListWidget(self.groupBox_5)
        self.listWidget_3.setObjectName("listWidget_3")
        self.verticalLayout_5.addWidget(self.listWidget_3)
        self.pushButton_als = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_als.setMinimumSize(QtCore.QSize(80, 30))
        self.pushButton_als.setMaximumSize(QtCore.QSize(80, 30))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/newPrefix/ico/分析.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_als.setIcon(icon4)
        self.pushButton_als.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_als.setObjectName("pushButton_als")
        self.verticalLayout_5.addWidget(self.pushButton_als, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_2.addWidget(self.groupBox_5)
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_6.setObjectName("groupBox_6")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.groupBox_6)
        self.tabWidget_2.setStyleSheet("#tabWidget_2>QWidget>QWidget{/*tab页*/\n"
"background-color: #444444;\n"
"}\n"
"#tabWidget_2::tab-bar{\n"
"alignment:left;/*tab位置*/\n"
"}\n"
"#tabWidget_2::pane { /*内容区域*/\n"
"background-color: rgb(80, 80, 80);/*背景色-空隙颜色*/\n"
"border:1px solid rgb(128, 128, 128);\n"
"} \n"
"#tabWidget_2 QTabBar{\n"
"color:white;\n"
"background-color:transparent;\n"
"}\n"
"#tabWidget_2 QTabBar::tab{/*页签*/\n"
"min-height:80px;\n"
"width:20px;\n"
"border-top-left-radius:20px;\n"
"border-bottom-right-radius:20px;\n"
"margin-right:1px;\n"
"margin-bottom:1px;\n"
"background-color:rgb(80, 80, 80);\n"
"}\n"
"#tabWidget_2 QTabBar::tab:hover{\n"
"color:black;\n"
"background-color: rgb(255, 170, 0);\n"
"border-bottom-right-radius:0px;\n"
"}\n"
"#tabWidget_2 QTabBar::tab:selected{\n"
"color:rgb(255, 170, 0);\n"
"border-bottom-right-radius:0px;\n"
"}\n"
"#tabWidget_2 QTabBar::tab:selected:hover{\n"
"color:black;\n"
"}\n"
"#tabWidget_2 QTabBar::tear{/*选项过多时的。。。*/\n"
"imag:;\n"
"}\n"
"#tabWidget_2 QTabBar::scroller{\n"
"width:60px;\n"
"}")
        self.tabWidget_2.setTabPosition(QtWidgets.QTabWidget.East)
        self.tabWidget_2.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget_2.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget_2.setUsesScrollButtons(True)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.tab_4)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_9.addLayout(self.verticalLayout_2)
        self.tabWidget_2.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.tab_5)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_10.addLayout(self.verticalLayout_6)
        self.tabWidget_2.addTab(self.tab_5, "")
        self.tab_13 = QtWidgets.QWidget()
        self.tab_13.setObjectName("tab_13")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.tab_13)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_11.addLayout(self.verticalLayout_7)
        self.tabWidget_2.addTab(self.tab_13, "")
        self.tab_12 = QtWidgets.QWidget()
        self.tab_12.setObjectName("tab_12")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.tab_12)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_12.addLayout(self.verticalLayout_8)
        self.tabWidget_2.addTab(self.tab_12, "")
        self.tab_11 = QtWidgets.QWidget()
        self.tab_11.setObjectName("tab_11")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.tab_11)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_13.addLayout(self.verticalLayout_9)
        self.tabWidget_2.addTab(self.tab_11, "")
        self.tab_10 = QtWidgets.QWidget()
        self.tab_10.setObjectName("tab_10")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.tab_10)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_14.addLayout(self.verticalLayout_10)
        self.tabWidget_2.addTab(self.tab_10, "")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.tab_9)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_15.addLayout(self.verticalLayout_11)
        self.tabWidget_2.addTab(self.tab_9, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.tab_8)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.horizontalLayout_16.addLayout(self.verticalLayout_12)
        self.tabWidget_2.addTab(self.tab_8, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.tab_7)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.horizontalLayout_17.addLayout(self.verticalLayout_13)
        self.tabWidget_2.addTab(self.tab_7, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.tab_6)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.horizontalLayout_18.addLayout(self.verticalLayout_14)
        self.tabWidget_2.addTab(self.tab_6, "")
        self.tab_15 = QtWidgets.QWidget()
        self.tab_15.setObjectName("tab_15")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.tab_15)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.horizontalLayout_19.addLayout(self.verticalLayout_15)
        self.tabWidget_2.addTab(self.tab_15, "")
        self.tab_14 = QtWidgets.QWidget()
        self.tab_14.setObjectName("tab_14")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.tab_14)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.horizontalLayout_20.addLayout(self.verticalLayout_16)
        self.tabWidget_2.addTab(self.tab_14, "")
        self.horizontalLayout_8.addWidget(self.tabWidget_2)
        self.horizontalLayout_2.addWidget(self.groupBox_6)
        self.tabWidget.addTab(self.tab_3, "")
        self.horizontalLayout_4.addWidget(self.tabWidget)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "全能数据分析王"))
        self.groupBox_2.setTitle(_translate("Form", "爬虫程序"))
        self.label_3.setText(_translate("Form", "查询页数："))
        self.label_4.setText(_translate("Form", "线程数量："))
        self.pushButton_run.setText(_translate("Form", "运行"))
        self.groupBox.setTitle(_translate("Form", "运行日志"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "数据抓取"))
        self.groupBox_3.setTitle(_translate("Form", "查询数据"))
        self.pushButton_del.setText(_translate("Form", "删除"))
        self.pushButton_sel.setText(_translate("Form", "查询"))
        self.groupBox_4.setTitle(_translate("Form", "查询结果"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "抓取ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "商品ID"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "标题"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "价格"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "分类"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "店铺"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "销售量"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "数据管理"))
        self.groupBox_5.setTitle(_translate("Form", "数据选取"))
        self.pushButton_als.setText(_translate("Form", "分析"))
        self.groupBox_6.setTitle(_translate("Form", "数据分析"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("Form", "分类销量占比"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), _translate("Form", "分类销量数"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_13), _translate("Form", "分类均价"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_12), _translate("Form", "分类评价"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_11), _translate("Form", "店铺销量占比"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_10), _translate("Form", "店铺销量数"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_9), _translate("Form", "店铺均价"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_8), _translate("Form", "店铺评价"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_7), _translate("Form", "销量及价格"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), _translate("Form", "好评及价格"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_15), _translate("Form", "中评及价格"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_14), _translate("Form", "差评及价格"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "数据分析"))
import image_rc
