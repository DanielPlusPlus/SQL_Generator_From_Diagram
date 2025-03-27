from PySide6.QtCore import QCoreApplication, QMetaObject, QRect
from PySide6.QtWidgets import QGridLayout, QHBoxLayout, QMenuBar, QStatusBar, QWidget


class MainWindowView(object):
    def setupUi(self, parentWindow):
        if not parentWindow.objectName():
            parentWindow.setObjectName(u"MainWindow")
        parentWindow.resize(800, 600)
        self.centralwidget = QWidget(parentWindow)
        self.centralwidget.setObjectName(u"Centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"GridLayout")
        self.horizontalLayout_1 = QHBoxLayout()
        self.horizontalLayout_1.setObjectName(u"HorizontalLayout_1")

        self.gridLayout.addLayout(self.horizontalLayout_1, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"HorizontalLayout_2")

        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        # self.gridLayout.setRowStretch(0, 1)
        # self.gridLayout.setRowStretch(1, 9)
        parentWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(parentWindow)
        self.menuBar.setObjectName(u"MenuBar")
        self.menuBar.setGeometry(QRect(0, 0, 800, 22))
        parentWindow.setMenuBar(self.menuBar)
        self.statusBar = QStatusBar(parentWindow)
        self.statusBar.setObjectName(u"StatusBar")
        parentWindow.setStatusBar(self.statusBar)
        self.retranslateUi(parentWindow)

        QMetaObject.connectSlotsByName(parentWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SQL generator from diagram", None))

    def addCentralWidget(self, widget):
        self.horizontalLayout_2.addWidget(widget)

    def updateStatusBar(self, message):
        self.statusBar.showMessage(message)

