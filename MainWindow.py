# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(892, 714)
        MainWindow.setMaximumSize(QtCore.QSize(892, 714))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.dwMain = QtWidgets.QDockWidget(self.centralwidget)
        self.dwMain.setAutoFillBackground(True)
        self.dwMain.setObjectName("dwMain")
        self.dockWidgetContents_5 = QtWidgets.QWidget()
        self.dockWidgetContents_5.setObjectName("dockWidgetContents_5")
        self.dwMain.setWidget(self.dockWidgetContents_5)
        self.horizontalLayout.addWidget(self.dwMain)
        self.dwIndicators = QtWidgets.QDockWidget(self.centralwidget)
        self.dwIndicators.setObjectName("dwIndicators")
        self.dockWidgetContents_3 = QtWidgets.QWidget()
        self.dockWidgetContents_3.setObjectName("dockWidgetContents_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.dockWidgetContents_3)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.groupBox_6 = QtWidgets.QGroupBox(self.dockWidgetContents_3)
        self.groupBox_6.setObjectName("groupBox_6")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.tableView_6 = QtWidgets.QTableView(self.groupBox_6)
        self.tableView_6.setObjectName("tableView_6")
        self.horizontalLayout_8.addWidget(self.tableView_6)
        self.groupBox_7 = QtWidgets.QGroupBox(self.groupBox_6)
        self.groupBox_7.setObjectName("groupBox_7")
        self.horizontalLayout_8.addWidget(self.groupBox_7)
        self.verticalLayout_8.addWidget(self.groupBox_6)
        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_8.addItem(spacerItem)
        self.textEdit = QtWidgets.QTextEdit(self.dockWidgetContents_3)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_8.addWidget(self.textEdit)
        self.dwIndicators.setWidget(self.dockWidgetContents_3)
        self.horizontalLayout.addWidget(self.dwIndicators)
        self.dwStrategyMonitor = QtWidgets.QDockWidget(self.centralwidget)
        self.dwStrategyMonitor.setObjectName("dwStrategyMonitor")
        self.dockWidgetContents_2 = QtWidgets.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.dwStrategyMonitor.setWidget(self.dockWidgetContents_2)
        self.horizontalLayout.addWidget(self.dwStrategyMonitor)
        self.dwTrade = QtWidgets.QDockWidget(self.centralwidget)
        self.dwTrade.setFloating(True)
        self.dwTrade.setFeatures(QtWidgets.QDockWidget.AllDockWidgetFeatures)
        self.dwTrade.setObjectName("dwTrade")
        self.dockWidgetContents_7 = QtWidgets.QWidget()
        self.dockWidgetContents_7.setMinimumSize(QtCore.QSize(159, 199))
        self.dockWidgetContents_7.setObjectName("dockWidgetContents_7")
        self.dwTrade.setWidget(self.dockWidgetContents_7)
        self.horizontalLayout.addWidget(self.dwTrade)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 892, 27))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menuStrategy = QtWidgets.QMenu(self.menubar)
        self.menuStrategy.setObjectName("menuStrategy")
        self.menuData = QtWidgets.QMenu(self.menubar)
        self.menuData.setObjectName("menuData")
        self.menuTA = QtWidgets.QMenu(self.menubar)
        self.menuTA.setObjectName("menuTA")
        self.menu_5 = QtWidgets.QMenu(self.menubar)
        self.menu_5.setObjectName("menu_5")
        self.menuTest = QtWidgets.QMenu(self.menubar)
        self.menuTest.setObjectName("menuTest")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBarStrategy = QtWidgets.QToolBar(MainWindow)
        self.toolBarStrategy.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.toolBarStrategy.setObjectName("toolBarStrategy")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBarStrategy)
        self.toolBarTeck = QtWidgets.QToolBar(MainWindow)
        self.toolBarTeck.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.toolBarTeck.setObjectName("toolBarTeck")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBarTeck)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.dwAccountMonitor = QtWidgets.QDockWidget(MainWindow)
        self.dwAccountMonitor.setMaximumSize(QtCore.QSize(892, 257))
        self.dwAccountMonitor.setAutoFillBackground(True)
        self.dwAccountMonitor.setFloating(True)
        self.dwAccountMonitor.setAllowedAreas(QtCore.Qt.BottomDockWidgetArea)
        self.dwAccountMonitor.setObjectName("dwAccountMonitor")
        self.dockWidgetContents_4 = QtWidgets.QWidget()
        self.dockWidgetContents_4.setObjectName("dockWidgetContents_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.dockWidgetContents_4)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.dockWidgetContents_4)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tab_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tblvwAccount = QtWidgets.QTableView(self.tab_3)
        self.tblvwAccount.setObjectName("tblvwAccount")
        self.horizontalLayout_3.addWidget(self.tblvwAccount)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.pbQryAccount = QtWidgets.QPushButton(self.groupBox_3)
        self.pbQryAccount.setObjectName("pbQryAccount")
        self.verticalLayout_7.addWidget(self.pbQryAccount)
        self.pbSaveAccount = QtWidgets.QPushButton(self.groupBox_3)
        self.pbSaveAccount.setObjectName("pbSaveAccount")
        self.verticalLayout_7.addWidget(self.pbSaveAccount)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_7.addWidget(self.pushButton_3)
        self.horizontalLayout_3.addWidget(self.groupBox_3)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.tab_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.tblvwHolding = QtWidgets.QTableView(self.tab_4)
        self.tblvwHolding.setObjectName("tblvwHolding")
        self.horizontalLayout_4.addWidget(self.tblvwHolding)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pbQryHolding = QtWidgets.QPushButton(self.groupBox_2)
        self.pbQryHolding.setObjectName("pbQryHolding")
        self.verticalLayout_4.addWidget(self.pbQryHolding)
        self.pbSaveHolding = QtWidgets.QPushButton(self.groupBox_2)
        self.pbSaveHolding.setObjectName("pbSaveHolding")
        self.verticalLayout_4.addWidget(self.pbSaveHolding)
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout_4.addWidget(self.pushButton_7)
        self.horizontalLayout_4.addWidget(self.groupBox_2)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.tblvwTrade = QtWidgets.QTableView(self.tab)
        self.tblvwTrade.setObjectName("tblvwTrade")
        self.horizontalLayout_5.addWidget(self.tblvwTrade)
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pbQryTrade = QtWidgets.QPushButton(self.groupBox)
        self.pbQryTrade.setObjectName("pbQryTrade")
        self.verticalLayout_2.addWidget(self.pbQryTrade)
        self.pbSaveTrade = QtWidgets.QPushButton(self.groupBox)
        self.pbSaveTrade.setObjectName("pbSaveTrade")
        self.verticalLayout_2.addWidget(self.pbSaveTrade)
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_2.addWidget(self.pushButton_6)
        self.horizontalLayout_5.addWidget(self.groupBox)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.tblveUntrade = QtWidgets.QTableView(self.tab_2)
        self.tblveUntrade.setObjectName("tblveUntrade")
        self.horizontalLayout_7.addWidget(self.tblveUntrade)
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.pbQryUnTrade = QtWidgets.QPushButton(self.groupBox_5)
        self.pbQryUnTrade.setObjectName("pbQryUnTrade")
        self.verticalLayout_6.addWidget(self.pbQryUnTrade)
        self.pbSaveUnTrade = QtWidgets.QPushButton(self.groupBox_5)
        self.pbSaveUnTrade.setObjectName("pbSaveUnTrade")
        self.verticalLayout_6.addWidget(self.pbSaveUnTrade)
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_6.addWidget(self.pushButton_5)
        self.horizontalLayout_7.addWidget(self.groupBox_5)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.tab_5)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.tblvwOrder = QtWidgets.QTableView(self.tab_5)
        self.tblvwOrder.setObjectName("tblvwOrder")
        self.horizontalLayout_6.addWidget(self.tblvwOrder)
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_5)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.pbQryOrder = QtWidgets.QPushButton(self.groupBox_4)
        self.pbQryOrder.setObjectName("pbQryOrder")
        self.verticalLayout_5.addWidget(self.pbQryOrder)
        self.pbSaveOrder = QtWidgets.QPushButton(self.groupBox_4)
        self.pbSaveOrder.setObjectName("pbSaveOrder")
        self.verticalLayout_5.addWidget(self.pbSaveOrder)
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_5.addWidget(self.pushButton_4)
        self.horizontalLayout_6.addWidget(self.groupBox_4)
        self.tabWidget.addTab(self.tab_5, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.dwAccountMonitor.setWidget(self.dockWidgetContents_4)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.dwAccountMonitor)
        self.dwManager = QtWidgets.QDockWidget(MainWindow)
        self.dwManager.setObjectName("dwManager")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.treeView = QtWidgets.QTreeView(self.dockWidgetContents)
        self.treeView.setObjectName("treeView")
        self.verticalLayout_3.addWidget(self.treeView)
        self.dwManager.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dwManager)
        self.actionLoginQuoteServer = QtWidgets.QAction(MainWindow)
        self.actionLoginQuoteServer.setObjectName("actionLoginQuoteServer")
        self.actionOpenAccount = QtWidgets.QAction(MainWindow)
        self.actionOpenAccount.setObjectName("actionOpenAccount")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionAaa = QtWidgets.QAction(MainWindow)
        self.actionAaa.setObjectName("actionAaa")
        self.actionTest1 = QtWidgets.QAction(MainWindow)
        self.actionTest1.setObjectName("actionTest1")
        self.actionOpenStrategy = QtWidgets.QAction(MainWindow)
        self.actionOpenStrategy.setObjectName("actionOpenStrategy")
        self.actionTestStrategy = QtWidgets.QAction(MainWindow)
        self.actionTestStrategy.setObjectName("actionTestStrategy")
        self.menu.addAction(self.actionLoginQuoteServer)
        self.menu.addAction(self.actionOpenAccount)
        self.menu.addSeparator()
        self.menu.addAction(self.actionExit)
        self.menuStrategy.addAction(self.actionAaa)
        self.menuTest.addAction(self.actionTest1)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menuStrategy.menuAction())
        self.menubar.addAction(self.menuData.menuAction())
        self.menubar.addAction(self.menuTA.menuAction())
        self.menubar.addAction(self.menuTest.menuAction())
        self.menubar.addAction(self.menu_5.menuAction())
        self.toolBarStrategy.addAction(self.actionOpenStrategy)
        self.toolBarStrategy.addAction(self.actionTestStrategy)
        self.toolBarStrategy.addSeparator()

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Boxigg交易系统"))
        self.dwIndicators.setWindowTitle(_translate("MainWindow", "指标管理"))
        self.groupBox_6.setTitle(_translate("MainWindow", "GroupBox"))
        self.groupBox_7.setTitle(_translate("MainWindow", "GroupBox"))
        self.dwStrategyMonitor.setWindowTitle(_translate("MainWindow", "策略监控"))
        self.dwTrade.setWindowTitle(_translate("MainWindow", "交易"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.menuStrategy.setTitle(_translate("MainWindow", "策略管理"))
        self.menuData.setTitle(_translate("MainWindow", "数据管理"))
        self.menuTA.setTitle(_translate("MainWindow", "技术分析"))
        self.menu_5.setTitle(_translate("MainWindow", "帮助"))
        self.menuTest.setTitle(_translate("MainWindow", "Test"))
        self.toolBarStrategy.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.toolBarTeck.setWindowTitle(_translate("MainWindow", "toolBar_2"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.dwAccountMonitor.setWindowTitle(_translate("MainWindow", "账户管理"))
        self.groupBox_3.setTitle(_translate("MainWindow", "GroupBox"))
        self.pbQryAccount.setText(_translate("MainWindow", "查询"))
        self.pbSaveAccount.setText(_translate("MainWindow", "保存"))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "账户"))
        self.groupBox_2.setTitle(_translate("MainWindow", "GroupBox"))
        self.pbQryHolding.setText(_translate("MainWindow", "查询"))
        self.pbSaveHolding.setText(_translate("MainWindow", "保存"))
        self.pushButton_7.setText(_translate("MainWindow", "PushButton"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "持仓"))
        self.groupBox.setTitle(_translate("MainWindow", "GroupBox"))
        self.pbQryTrade.setText(_translate("MainWindow", "查询"))
        self.pbSaveTrade.setText(_translate("MainWindow", "保存"))
        self.pushButton_6.setText(_translate("MainWindow", "PushButton"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "成交"))
        self.groupBox_5.setTitle(_translate("MainWindow", "GroupBox"))
        self.pbQryUnTrade.setText(_translate("MainWindow", "查询"))
        self.pbSaveUnTrade.setText(_translate("MainWindow", "保存"))
        self.pushButton_5.setText(_translate("MainWindow", "PushButton"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "未成交"))
        self.groupBox_4.setTitle(_translate("MainWindow", "GroupBox"))
        self.pbQryOrder.setText(_translate("MainWindow", "查询"))
        self.pbSaveOrder.setText(_translate("MainWindow", "保存"))
        self.pushButton_4.setText(_translate("MainWindow", "PushButton"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "委托"))
        self.dwManager.setWindowTitle(_translate("MainWindow", "管理面板"))
        self.actionLoginQuoteServer.setText(_translate("MainWindow", "登录行情服务器"))
        self.actionOpenAccount.setText(_translate("MainWindow", "OpenAccount"))
        self.actionExit.setText(_translate("MainWindow", "退出"))
        self.actionAaa.setText(_translate("MainWindow", "参数优化"))
        self.actionAaa.setToolTip(_translate("MainWindow", "参数优化"))
        self.actionTest1.setText(_translate("MainWindow", "Test1"))
        self.actionOpenStrategy.setText(_translate("MainWindow", "OpenStrategy"))
        self.actionTestStrategy.setText(_translate("MainWindow", "TestStrategy"))

