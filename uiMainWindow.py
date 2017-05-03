# encoding: UTF-8

import psutil

from ctpquant.uiBasicWidget import *
from ctpquant.ctaAlgo.uiCtaWidget import CtaEngineManager
from ctpquant.dataRecorder.uiDrWidget import DrEngineManager
from ctpquant.riskManager.uiRmWidget import RmEngineManager
from ctpquant.engine import MainEngine, QuoteEngine

########################################################################
class MainWindow(QtWidgets.QMainWindow):
    """主窗口"""
    signalStatusBar = QtCore.pyqtSignal(type(Event()))

    def __init__(self):
        """Constructor"""
        super(MainWindow, self).__init__()

        self.quoteEngine = QuoteEngine()
        self.quoteEventEngine = self.quoteEngine.eventEngine
        time.sleep(1)

        self.mainEngine = MainEngine(self.quoteEngine)
        self.eventEngine = self.mainEngine.eventEngine
        time.sleep(1)

        #
        # self.mainEngine = mainEngine
        # self.eventEngine = mainEngine.eventEngine
        # self.quoteEngine = quoteEngine
        # self.quoteEventEngine = quoteEngine.eventEngine

        # self.connectCtpQuote()

        self.widgetDict = {}    # 用来保存子窗口的字典
        
        self.initUi()
        self.loadWindowSettings()

    def initUi(self):
        """初始化界面"""
        self.setWindowTitle('CTPQuant')
        self.initCentral()
        self.initMenu()
        #self.initStatusBar()

    def initCentral(self):
        """初始化中心区域"""
        widgetMarketM, dockMarketM = self.createMarketMonitor(MarketMonitor, '行情', QtCore.Qt.RightDockWidgetArea)
        widgetContractM, dockContractM = self.createDock(ContractMonitor, '合约列表', QtCore.Qt.RightDockWidgetArea)
        widgetLogM, dockLogM = self.createDock(LogMonitor, '日志', QtCore.Qt.BottomDockWidgetArea)
        widgetErrorM, dockErrorM = self.createDock(ErrorMonitor, '错误', QtCore.Qt.BottomDockWidgetArea)
        widgetTradeM, dockTradeM = self.createDock(TradeMonitor, '成交', QtCore.Qt.RightDockWidgetArea)
        widgetOrderM, dockOrderM = self.createDock(OrderMonitor, '委托', QtCore.Qt.RightDockWidgetArea)
        widgetUTOrderM, dockUTOrderM = self.createDock(UTOrderMonitor, '未成交委托', QtCore.Qt.RightDockWidgetArea)
        widgetPositionM, dockPositionM = self.createDock(PositionMonitor, '持仓', QtCore.Qt.BottomDockWidgetArea)
        widgetAccountM, dockAccountM = self.createDock(AccountMonitor, '账户', QtCore.Qt.BottomDockWidgetArea)
        widgetTradingW, dockTradingW = self.createDock(TradingWidget, '交易', QtCore.Qt.LeftDockWidgetArea)
    
        self.tabifyDockWidget(dockMarketM, dockContractM)
        self.tabifyDockWidget(dockLogM, dockErrorM)
        self.tabifyDockWidget(dockTradeM, dockUTOrderM)
        self.tabifyDockWidget(dockUTOrderM, dockOrderM)
        self.tabifyDockWidget(dockPositionM, dockAccountM)


        dockLogM.raise_()
        dockPositionM.raise_()
        dockUTOrderM.raise_()
    
        # 连接组件之间的信号
        widgetPositionM.itemDoubleClicked.connect(widgetTradingW.closePosition)

    def initMenu(self):
        """初始化菜单"""
        # 创建操作
        connectCtpQuoteAction = QtWidgets.QAction(u'连接CTP行情', self)
        connectCtpQuoteAction.triggered.connect(self.connectCtpQuote)
        connectCtpAction = QtWidgets.QAction(u'连接账户', self)
        connectCtpAction.triggered.connect(self.connectCtp)
        '''
        connectLtsAction = QtWidgets.QAction(u'连接LTS', self)
        connectLtsAction.triggered.connect(self.connectLts)
        
        connectKsotpAction = QtWidgets.QAction(u'连接金仕达期权', self)
        connectKsotpAction.triggered.connect(self.connectKsotp)
        
        connectFemasAction = QtWidgets.QAction(u'连接飞马', self)
        connectFemasAction.triggered.connect(self.connectFemas)  
        
        connectXspeedAction = QtWidgets.QAction(u'连接飞创', self)
        connectXspeedAction.triggered.connect(self.connectXspeed)          
        
        connectKsgoldAction = QtWidgets.QAction(u'连接金仕达黄金', self)
        connectKsgoldAction.triggered.connect(self.connectKsgold)  
        
        connectSgitAction = QtWidgets.QAction(u'连接飞鼠', self)
        connectSgitAction.triggered.connect(self.connectSgit)         
        
        connectWindAction = QtWidgets.QAction(u'连接Wind', self)
        connectWindAction.triggered.connect(self.connectWind)
        
        connectIbAction = QtWidgets.QAction(u'连接IB', self)
        connectIbAction.triggered.connect(self.connectIb) 
        
        connectOandaAction = QtWidgets.QAction(u'连接OANDA', self)
        connectOandaAction.triggered.connect(self.connectOanda)
        
        connectOkcoinAction = QtWidgets.QAction(u'连接OKCOIN', self)
        connectOkcoinAction.triggered.connect(self.connectOkcoin)        
        '''
        connectDbAction = QtWidgets.QAction(u'连接数据库', self)
        connectDbAction.triggered.connect(self.mainEngine.dbConnect)
        
        testAction = QtWidgets.QAction(u'测试', self)
        testAction.triggered.connect(self.test)
        
        exitAction = QtWidgets.QAction(u'退出', self)
        exitAction.triggered.connect(self.close)
        
        aboutAction = QtWidgets.QAction(u'关于', self)
        aboutAction.triggered.connect(self.openAbout)
        
        contractAction = QtWidgets.QAction(u'查询合约', self)
        contractAction.triggered.connect(self.openContract)
        
        drAction = QtWidgets.QAction(u'行情数据记录', self)
        drAction.triggered.connect(self.openDr)
        
        ctaAction = QtWidgets.QAction(u'CTA策略', self)
        ctaAction.triggered.connect(self.openCta)
        
        rmAction = QtWidgets.QAction(u'风险管理', self)
        rmAction.triggered.connect(self.openRm)

        qryAccountAction = QtWidgets.QAction('账户查询', self)
        qryAccountAction.triggered.connect(self.qryAccount)

        qryInvestorPositionAction = QtWidgets.QAction('持仓查询', self)
        qryInvestorPositionAction.triggered.connect(self.qryInvestorPosition)

        # 创建菜单
        menubar = self.menuBar()
        
        # 设计为只显示存在的接口
        sysMenu = menubar.addMenu(u'系统')
        if 'CTPTrade' in self.mainEngine.gatewayDict:
            sysMenu.addAction(connectCtpAction)
        if 'CTPQuote' in self.quoteEngine.gatewayDict:
            sysMenu.addAction(connectCtpQuoteAction)
        # if 'LTS' in self.mainEngine.gatewayDict:
        #     sysMenu.addAction(connectLtsAction)
        # if 'FEMAS' in self.mainEngine.gatewayDict:
        #     sysMenu.addAction(connectFemasAction)
        # if 'XSPEED' in self.mainEngine.gatewayDict:
        #     sysMenu.addAction(connectXspeedAction)
        # if 'KSOTP' in self.mainEngine.gatewayDict:
        #     sysMenu.addAction(connectKsotpAction)
        # if 'KSGOLD' in self.mainEngine.gatewayDict:
        #     sysMenu.addAction(connectKsgoldAction)
        # if 'SGIT' in self.mainEngine.gatewayDict:
        #     sysMenu.addAction(connectSgitAction)
        # sysMenu.addSeparator()
        # if 'IB' in self.mainEngine.gatewayDict:
        #     sysMenu.addAction(connectIbAction)
        # if 'OANDA' in self.mainEngine.gatewayDict:
        #     sysMenu.addAction(connectOandaAction)
        # if 'OKCOIN' in self.mainEngine.gatewayDict:
        #     sysMenu.addAction(connectOkcoinAction)
        # sysMenu.addSeparator()
        # if 'Wind' in self.mainEngine.gatewayDict:
        #     sysMenu.addAction(connectWindAction)
        sysMenu.addSeparator()
        sysMenu.addAction(connectDbAction)
        sysMenu.addSeparator()
        sysMenu.addAction(exitAction)
        
        functionMenu = menubar.addMenu('功能')
        functionMenu.addAction(contractAction)
        functionMenu.addAction(drAction)
        functionMenu.addAction(rmAction)
        functionMenu.addSeparator()
        functionMenu.addAction(qryAccountAction)
        functionMenu.addAction(qryInvestorPositionAction)

        # 算法相关
        algoMenu = menubar.addMenu('策略')
        algoMenu.addAction(ctaAction)
        
        # 帮助
        helpMenu = menubar.addMenu('帮助')
        helpMenu.addAction(aboutAction)  
        helpMenu.addAction(testAction)

    def initStatusBar(self):
        """初始化状态栏"""
        self.statusLabel = QtWidgets.QLabel()
        self.statusLabel.setAlignment(QtCore.Qt.AlignLeft)
        
        self.statusBar().addPermanentWidget(self.statusLabel)
        self.statusLabel.setText(self.getCpuMemory())
        
        self.sbCount = 0
        self.sbTrigger = 10     # 10秒刷新一次
        self.signalStatusBar.connect(self.updateStatusBar)
        self.eventEngine.register(EVENT_TIMER, self.signalStatusBar.emit)

    def updateStatusBar(self, event):
        """在状态栏更新CPU和内存信息"""
        self.sbCount += 1
        
        if self.sbCount == self.sbTrigger:
            self.sbCount = 0
            self.statusLabel.setText(self.getCpuMemory())

    def getCpuMemory(self):
        """获取CPU和内存状态信息"""
        cpuPercent = psutil.cpu_percent()
        memoryPercent = psutil.virtual_memory().percent
        return u'CPU使用率：%d%%   内存使用率：%d%%' % (cpuPercent, memoryPercent)        

    def connectCtp(self):
        """连接CTP接口"""
        self.mainEngine.connect('CTPTrade')

    def connectCtpQuote(self):
        """连接CTP行情接口"""
        self.quoteEngine.connect('CTPQuote')

    def test(self):
        """测试按钮用的函数"""
        # 有需要使用手动触发的测试函数可以写在这里
        pass
    #--------------------------------------------------------------------
    def qryAccount(self):
        self.mainEngine.gatewayDict['CTPTrade'].qryAccount()
    #--------------------------------------------------------------------
    def qryInvestorPosition(self):
        self.mainEngine.gatewayDict['CTPTrade'].qryPosition()
    #--------------------------------------------------------------------
    def openAbout(self):
        """打开关于"""
        try:
            self.widgetDict['aboutW'].show()
        except KeyError:
            self.widgetDict['aboutW'] = AboutWidget(self)
            self.widgetDict['aboutW'].show()

    def openContract(self):
        """打开合约查询"""
        self.mainEngine.gatewayDict['CTPTrade'].qryInstrument()
        time.sleep(5)
        try:
            self.widgetDict['contractM'].show()
        except KeyError:
            self.widgetDict['contractM'] = ContractMonitor(self.mainEngine,self.eventEngine)
            self.widgetDict['contractM'].show()
    
    def openCta(self):
        """打开CTA组件"""
        try:
            self.widgetDict['ctaM'].showMaximized()
        except KeyError:
            self.widgetDict['ctaM'] = CtaEngineManager(self.mainEngine.ctaEngine, self.eventEngine)
            self.widgetDict['ctaM'].showMaximized()
    
    def openDr(self):
        """打开行情数据记录组件"""
        try:
            self.widgetDict['drM'].showMaximized()
        except KeyError:
            self.widgetDict['drM'] = DrEngineManager(self.quoteEngine.drEngine, self.quoteEventEngine)
            self.widgetDict['drM'].showMaximized()
    
    def openRm(self):
        """打开组件"""
        try:
            self.widgetDict['rmM'].show()
        except KeyError:
            self.widgetDict['rmM'] = RmEngineManager(self.mainEngine.rmEngine, self.eventEngine)
            self.widgetDict['rmM'].show()      

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
    
    def createDock(self, widgetClass, widgetName, widgetArea):
        """创建停靠组件"""
        widget = widgetClass(self.mainEngine, self.eventEngine)
        dock = QtWidgets.QDockWidget(widgetName)
        dock.setWidget(widget)
        dock.setObjectName(widgetName)
        dock.setFeatures(dock.DockWidgetFloatable|dock.DockWidgetMovable)
        self.addDockWidget(widgetArea, dock)
        return widget, dock

    def createMarketMonitor(self, widgetClass, widgetName, widgetArea):
        """创建停靠组件"""
        widget = widgetClass(self.quoteEngine, self.quoteEventEngine)
        # widget = widgetClass(self.quoteEngine, self.quoteEventEngine)
        dock = QtWidgets.QDockWidget(widgetName)
        dock.setWidget(widget)
        dock.setObjectName(widgetName)
        dock.setFeatures(dock.DockWidgetFloatable|dock.DockWidgetMovable)
        self.addDockWidget(widgetArea, dock)
        return widget, dock

    def saveWindowSettings(self):
        """保存窗口设置"""
        settings = QtCore.QSettings('vn.py', 'vn.trader')
        settings.setValue('state', self.saveState())
        settings.setValue('geometry', self.saveGeometry())

    def loadWindowSettings(self):
        """载入窗口设置"""
        settings = QtCore.QSettings('vn.py', 'vn.trader')
        # 这里由于PyQt4的版本不同，settings.value('state')调用返回的结果可能是：
        # 1. None（初次调用，注册表里无相应记录，因此为空）
        # 2. QByteArray（比较新的PyQt4）
        # 3. QVariant（以下代码正确执行所需的返回结果）
        # 所以为了兼容考虑，这里加了一个try...except，如果是1、2的情况就pass
        # 可能导致主界面的设置无法载入（每次退出时的保存其实是成功了）
        try:
            self.restoreState(settings.value('state').toByteArray())
            self.restoreGeometry(settings.value('geometry').toByteArray())    
        except AttributeError:
            pass


class AboutWidget(QtWidgets.QDialog):
    """显示关于信息"""

    def __init__(self, parent=None):
        """Constructor"""
        super(AboutWidget, self).__init__(parent)

        self.initUi()

    def initUi(self):
        """"""
        self.setWindowTitle(u'关于VnTrader')

        text = u"""
            Developed by traders, for traders.

            License：MIT
            
            Website：www.vnpy.org

            Github：www.github.com/vnpy/vnpy
            
            """

        label = QtWidgets.QLabel()
        label.setText(text)
        label.setMinimumWidth(500)

        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(label)

        self.setLayout(vbox)
    