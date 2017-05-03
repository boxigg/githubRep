# encoding: UTF-8

import sys
import ctypes
import platform
import importlib
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore,  QtWidgets,QtGui
from collections import OrderedDict
import time

from ctpquant.engine import MainEngine, QuoteEngine
# from ctpquant.uiMainWindow import *
from ctpquant.uiBasicWidget import *
from ctpquant.ui.MainWindow import Ui_MainWindow

class MainUI(QMainWindow, Ui_MainWindow):#从自动生成的界面类继承

    def __init__(self, mainEngine=None, quoteEngine=None):
        """Constructor"""
        super(MainUI, self).__init__()

        if quoteEngine is None:
            self.quoteEngine = QuoteEngine()
            self.quoteEventEngine = self.quoteEngine.eventEngine
            time.sleep(1)
        else:
            self.quoteEngine=quoteEngine
            self.quoteEventEngine=self.quoteEngine.eventEngine

        if mainEngine is None:
            self.mainEngine = MainEngine(self.quoteEngine)
            self.eventEngine = self.mainEngine.eventEngine
            time.sleep(1)
        else:
            self.mainEngine = mainEngine
            self.eventEngine = self.mainEngine.eventEngine

        self.widgetDict = {}  # 用来保存子窗口的字典

        self.tickHeaderDic = OrderedDict()

        self.setupUi(self)

        self.regEvent()
        self.iniTableWidgets()
        # self.arrangeDW()

    def iniTableWidgets(self):
        # widgetMarketM, dockMarketM = self.createMarketMonitor(MarketMonitor, '行情', QtCore.Qt.AllDockWidgetAreas,parent = self.tabQuote)
        # self.tabWidgetMain.maximumSize()
        pass

    def regEvent(self):
        self.actionLoginQuoteServer.triggered.connect(self.connectCtpQuote)
        self.actionExit.triggered.connect(self.close)



    def iniTableHeaderDic(self):
        # 设置表头有序字典

        self.tickHeaderDic['symbol'] = {'chinese': u'合约代码', 'cellType': BasicCell}
        self.tickHeaderDic['vtSymbol'] = {'chinese': u'名称', 'cellType': NameCell}
        self.tickHeaderDic['lastPrice'] = {'chinese': u'最新价', 'cellType': BasicCell}
        self.tickHeaderDic['preClosePrice'] = {'chinese': u'昨收盘价', 'cellType': BasicCell}
        self.tickHeaderDic['volume'] = {'chinese': u'成交量', 'cellType': BasicCell}
        self.tickHeaderDic['openInterest'] = {'chinese': u'持仓量', 'cellType': BasicCell}
        self.tickHeaderDic['openPrice'] = {'chinese': u'开盘价', 'cellType': BasicCell}
        self.tickHeaderDic['highPrice'] = {'chinese': u'最高价', 'cellType': BasicCell}
        self.tickHeaderDic['lowPrice'] = {'chinese': u'最低价', 'cellType': BasicCell}
        self.tickHeaderDic['bidPrice1'] = {'chinese': u'买一价', 'cellType': BidCell}
        self.tickHeaderDic['bidVolume1'] = {'chinese': u'买一量', 'cellType': BidCell}
        self.tickHeaderDic['askPrice1'] = {'chinese': u'卖一价', 'cellType': AskCell}
        self.tickHeaderDic['askVolume1'] = {'chinese': u'卖一量', 'cellType': AskCell}
        self.tickHeaderDic['time'] = {'chinese': u'时间', 'cellType': BasicCell}
        self.tickHeaderDic['gatewayName'] = {'chinese': u'接口', 'cellType': BasicCell}

    def  connectCtpQuote(self):
        """连接CTP行情接口"""
        self.quoteEngine.connect('CTPQuote')

    def createDock(self, widgetClass, widgetName, widgetArea,parent = None):
        """创建停靠组件"""
        widget = widgetClass(self.mainEngine, self.eventEngine,parent=parent)

        dock = QtWidgets.QDockWidget(widgetName)
        dock.setWidget(widget)
        dock.setObjectName(widgetName)
        dock.setFeatures(dock.DockWidgetFloatable|dock.DockWidgetMovable)
        self.addDockWidget(widgetArea, dock)
        return widget, dock

    def arrangeDW(self):
        self.splitDockWidget(self.dwManager,self.dwMain,QtCore.Qt.Horizontal )


    def createMarketMonitor(self, widgetClass, widgetName, widgetArea,parent = None):
        """创建停靠组件"""
        widget = widgetClass(self.quoteEngine, self.quoteEventEngine,parent = parent)

        dock = QtWidgets.QDockWidget(widgetName)
        dock.setWidget(widget)
        dock.setObjectName(widgetName)
        dock.setFeatures(dock.DockWidgetFloatable|dock.DockWidgetMovable)
        self.addDockWidget(widgetArea, dock)
        return widget, dock

    def closeEvent(self, event):
        """关闭事件"""
        reply = QtWidgets.QMessageBox.question(self, '退出',
                                               '确认退出?', QtWidgets.QMessageBox.Yes |
                                               QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            for widget in self.widgetDict.values():
                widget.close()
            self.saveWindowSettings()

            self.mainEngine.exit()
            self.quoteEngine.exit()
            event.accept()
        else:
            event.ignore()

# ----------------------------------------------------------------------
def main():
    """主程序入口"""
    # 重载sys模块，设置默认字符串编码方式为utf8
    importlib.reload(sys)
    # sys.setdefaultencoding('utf8')

    # 设置Windows底部任务栏图标
    if 'Windows' in platform.uname():
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('BoxiQuant')

    # 初始化Qt应用对象
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('vnpy.ico'))
    # app.setFont(BASIC_FONT)

    # 设置Qt的皮肤
    try:
        f = open("VT_setting.json")
        setting = json.load(f)
        print(setting)
        if setting['darkStyle']:
            import qdarkstyle
            app.setStyleSheet(qdarkstyle.load_stylesheet(pyside=False))
    except:
        pass

    # 初始化主引擎和主窗口对象
    # mainEngine = MainEngine()
    # quoteEngine = QuoteEngine()
    time.sleep(2)
    mainWindow = MainUI()
    mainWindow.showMaximized()

    # 在主线程中启动Qt事件循环
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
