# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGraphicsView, QHBoxLayout,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QVBoxLayout, QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 633)
        palette = QPalette()
        MainWindow.setPalette(palette)
        MainWindow.setContextMenuPolicy(Qt.NoContextMenu)
        MainWindow.setStyleSheet(u"QMenuBar {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #f18701, stop:1 #f7b801);\n"
"    spacing: 3px;\n"
"}\n"
"QMenuBar::item {\n"
"	padding: 1px 4px;\n"
"    background: transparent;\n"
"    border-radius: 4px 4px 0px 0px;\n"
"}\n"
"QMenuBar::item:selected { /* when selected using mouse or keyboard */\n"
"    background: #f7b801;\n"
"}\n"
"\n"
"QMenu {\n"
"	background-color: #f7b801;\n"
"}")
        self.docsAction = QAction(MainWindow)
        self.docsAction.setObjectName(u"docsAction")
        self.aboutAction = QAction(MainWindow)
        self.aboutAction.setObjectName(u"aboutAction")
        self.newFieldAction = QAction(MainWindow)
        self.newFieldAction.setObjectName(u"newFieldAction")
        self.openFieldAction = QAction(MainWindow)
        self.openFieldAction.setObjectName(u"openFieldAction")
        self.saveFieldAction = QAction(MainWindow)
        self.saveFieldAction.setObjectName(u"saveFieldAction")
        self.cleanFieldAction = QAction(MainWindow)
        self.cleanFieldAction.setObjectName(u"cleanFieldAction")
        self.calcFieldAction = QAction(MainWindow)
        self.calcFieldAction.setObjectName(u"calcFieldAction")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0  #3d348b, stop:1 #7678ed);\n"
"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.fieldGraphicsView = QGraphicsView(self.centralwidget)
        self.fieldGraphicsView.setObjectName(u"fieldGraphicsView")
        self.fieldGraphicsView.setStyleSheet(u"border: 2px solid white;\n"
"border-radius: 5px;")

        self.verticalLayout.addWidget(self.fieldGraphicsView)

        self.horizontalFrame = QFrame(self.centralwidget)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        self.horizontalFrame.setStyleSheet(u" background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #f18701, stop:1 #f7b801);\n"
"border-radius: 5px;\n"
"padding: 0px;")
        self.tools_layout = QHBoxLayout(self.horizontalFrame)
        self.tools_layout.setObjectName(u"tools_layout")
        self.jumpBackwardButton = QPushButton(self.horizontalFrame)
        self.jumpBackwardButton.setObjectName(u"jumpBackwardButton")
        self.jumpBackwardButton.setStyleSheet(u"QPushButton{\n"
"	padding: 5px;\n"
"	background: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #f7b801;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: #f35b04;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/icons/skip_previous.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.jumpBackwardButton.setIcon(icon)
        self.jumpBackwardButton.setIconSize(QSize(24, 24))

        self.tools_layout.addWidget(self.jumpBackwardButton)

        self.frameSpinBox = QSpinBox(self.horizontalFrame)
        self.frameSpinBox.setObjectName(u"frameSpinBox")
        self.frameSpinBox.setStyleSheet(u"QSpinBox {\n"
"	padding: 5px;\n"
"	font-size: 14pt;\n"
"	background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.65 rgba(255, 255, 255, 255), stop:0.66 transparent, stop:1 transparent);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QSpinBox::up-button {\n"
"	background-color: transparent;\n"
"	border-top-right-radius: 5px;\n"
"	width: 20px; height: 20px;\n"
"	subcontrol-origin: border;\n"
"	subcontrol-position: top right;\n"
"	image: url(:/icons/icons/arrow_drop_up.svg);\n"
"}\n"
"\n"
"QSpinBox::down-button {\n"
"	background-color: transparent;\n"
"	border-bottom-right-radius: 5px;\n"
"	width: 20px; height: 20px;\n"
"	subcontrol-origin: border;\n"
"	subcontrol-position: bottom right;\n"
"	image: url(:/icons/icons/arrow_drop_down.svg);\n"
"}\n"
"\n"
"QSpinBox::up-button:hover {\n"
"	background-color: #f7b801;\n"
"}\n"
"QSpinBox::up-button:pressed {\n"
"	background-color: #f35b04;\n"
"}\n"
"\n"
"QSpinBox::down-button:hover {\n"
"	background-color: #f7b801;\n"
"}\n"
"QSpi"
                        "nBox::down-button:pressed {\n"
"	background-color: #f35b04;\n"
"}")

        self.tools_layout.addWidget(self.frameSpinBox)

        self.stopButton = QPushButton(self.horizontalFrame)
        self.stopButton.setObjectName(u"stopButton")
        self.stopButton.setStyleSheet(u"QPushButton{\n"
"	padding: 5px;\n"
"	background: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #f7b801;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: #f35b04;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/stop.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.stopButton.setIcon(icon1)
        self.stopButton.setIconSize(QSize(24, 24))

        self.tools_layout.addWidget(self.stopButton)

        self.playButton = QPushButton(self.horizontalFrame)
        self.playButton.setObjectName(u"playButton")
        self.playButton.setStyleSheet(u"QPushButton{\n"
"	padding: 5px;\n"
"	background: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #f7b801;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: #f35b04;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/play_arrow.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.playButton.setIcon(icon2)
        self.playButton.setIconSize(QSize(24, 24))

        self.tools_layout.addWidget(self.playButton)

        self.jumpForwardButton = QPushButton(self.horizontalFrame)
        self.jumpForwardButton.setObjectName(u"jumpForwardButton")
        self.jumpForwardButton.setStyleSheet(u"QPushButton{\n"
"	padding: 5px;\n"
"	background: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #f7b801;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: #f35b04;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/skip_next.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.jumpForwardButton.setIcon(icon3)
        self.jumpForwardButton.setIconSize(QSize(24, 24))

        self.tools_layout.addWidget(self.jumpForwardButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.tools_layout.addItem(self.horizontalSpacer)

        self.modeLabel = QLabel(self.horizontalFrame)
        self.modeLabel.setObjectName(u"modeLabel")
        self.modeLabel.setStyleSheet(u"QLabel {\n"
"background-color: rgba(0,0,0,0);\n"
"}")

        self.tools_layout.addWidget(self.modeLabel)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.tools_layout.addItem(self.horizontalSpacer_2)

        self.paletteButton = QPushButton(self.horizontalFrame)
        self.paletteButton.setObjectName(u"paletteButton")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.paletteButton.sizePolicy().hasHeightForWidth())
        self.paletteButton.setSizePolicy(sizePolicy)

        self.tools_layout.addWidget(self.paletteButton)

        self.drawButton = QPushButton(self.horizontalFrame)
        self.drawButton.setObjectName(u"drawButton")
        self.drawButton.setStyleSheet(u"QPushButton{\n"
"	padding: 5px;\n"
"	background: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #f7b801;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: #f35b04;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/brush.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.drawButton.setIcon(icon4)
        self.drawButton.setIconSize(QSize(24, 24))

        self.tools_layout.addWidget(self.drawButton)

        self.eraseButton = QPushButton(self.horizontalFrame)
        self.eraseButton.setObjectName(u"eraseButton")
        self.eraseButton.setStyleSheet(u"QPushButton{\n"
"	padding: 5px;\n"
"	background: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #f7b801;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: #f35b04;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/ink_eraser.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.eraseButton.setIcon(icon5)
        self.eraseButton.setIconSize(QSize(24, 24))

        self.tools_layout.addWidget(self.eraseButton)


        self.verticalLayout.addWidget(self.horizontalFrame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setEnabled(True)
        self.menuBar.setGeometry(QRect(0, 0, 800, 19))
        palette1 = QPalette()
        gradient = QLinearGradient(0, 0, 0, 1)
        gradient.setSpread(QGradient.PadSpread)
        gradient.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient.setColorAt(0, QColor(241, 135, 1, 255))
        gradient.setColorAt(1, QColor(247, 184, 1, 255))
        brush = QBrush(gradient)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush)
        gradient1 = QLinearGradient(0, 0, 0, 1)
        gradient1.setSpread(QGradient.PadSpread)
        gradient1.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient1.setColorAt(0, QColor(241, 135, 1, 255))
        gradient1.setColorAt(1, QColor(247, 184, 1, 255))
        brush1 = QBrush(gradient1)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        gradient2 = QLinearGradient(0, 0, 0, 1)
        gradient2.setSpread(QGradient.PadSpread)
        gradient2.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient2.setColorAt(0, QColor(241, 135, 1, 255))
        gradient2.setColorAt(1, QColor(247, 184, 1, 255))
        brush2 = QBrush(gradient2)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush2)
        gradient3 = QLinearGradient(0, 0, 0, 1)
        gradient3.setSpread(QGradient.PadSpread)
        gradient3.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient3.setColorAt(0, QColor(241, 135, 1, 255))
        gradient3.setColorAt(1, QColor(247, 184, 1, 255))
        brush3 = QBrush(gradient3)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush3)
        gradient4 = QLinearGradient(0, 0, 0, 1)
        gradient4.setSpread(QGradient.PadSpread)
        gradient4.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient4.setColorAt(0, QColor(241, 135, 1, 255))
        gradient4.setColorAt(1, QColor(247, 184, 1, 255))
        brush4 = QBrush(gradient4)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        gradient5 = QLinearGradient(0, 0, 0, 1)
        gradient5.setSpread(QGradient.PadSpread)
        gradient5.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient5.setColorAt(0, QColor(241, 135, 1, 255))
        gradient5.setColorAt(1, QColor(247, 184, 1, 255))
        brush5 = QBrush(gradient5)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush5)
        gradient6 = QLinearGradient(0, 0, 0, 1)
        gradient6.setSpread(QGradient.PadSpread)
        gradient6.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient6.setColorAt(0, QColor(241, 135, 1, 255))
        gradient6.setColorAt(1, QColor(247, 184, 1, 255))
        brush6 = QBrush(gradient6)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush6)
        gradient7 = QLinearGradient(0, 0, 0, 1)
        gradient7.setSpread(QGradient.PadSpread)
        gradient7.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient7.setColorAt(0, QColor(241, 135, 1, 255))
        gradient7.setColorAt(1, QColor(247, 184, 1, 255))
        brush7 = QBrush(gradient7)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        gradient8 = QLinearGradient(0, 0, 0, 1)
        gradient8.setSpread(QGradient.PadSpread)
        gradient8.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient8.setColorAt(0, QColor(241, 135, 1, 255))
        gradient8.setColorAt(1, QColor(247, 184, 1, 255))
        brush8 = QBrush(gradient8)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush8)
        self.menuBar.setPalette(palette1)
        self.fileMenu = QMenu(self.menuBar)
        self.fileMenu.setObjectName(u"fileMenu")
        self.helpMenu = QMenu(self.menuBar)
        self.helpMenu.setObjectName(u"helpMenu")
        self.editMenu = QMenu(self.menuBar)
        self.editMenu.setObjectName(u"editMenu")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.fileMenu.menuAction())
        self.menuBar.addAction(self.editMenu.menuAction())
        self.menuBar.addAction(self.helpMenu.menuAction())
        self.fileMenu.addAction(self.newFieldAction)
        self.fileMenu.addAction(self.openFieldAction)
        self.fileMenu.addAction(self.saveFieldAction)
        self.helpMenu.addAction(self.docsAction)
        self.helpMenu.addAction(self.aboutAction)
        self.editMenu.addAction(self.cleanFieldAction)
        self.editMenu.addAction(self.calcFieldAction)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Life Odyssey", None))
        self.docsAction.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0430\u0446\u0438\u044f", None))
        self.aboutAction.setText(QCoreApplication.translate("MainWindow", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
        self.newFieldAction.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u043e\u0435 \u043f\u043e\u043b\u0435", None))
        self.openFieldAction.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u043f\u043e\u043b\u0435", None))
        self.saveFieldAction.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043f\u043e\u043b\u0435", None))
        self.cleanFieldAction.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u043f\u043e\u043b\u0435", None))
        self.calcFieldAction.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0447\u0438\u0442\u0430\u0442\u044c \u0438\u0442\u0435\u0440\u0430\u0446\u0438\u0438", None))
        self.jumpBackwardButton.setText("")
        self.stopButton.setText("")
        self.playButton.setText("")
        self.jumpForwardButton.setText("")
        self.modeLabel.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0436\u0438\u043c: \u0440\u0438\u0441\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.paletteButton.setText("")
        self.drawButton.setText("")
        self.eraseButton.setText("")
        self.fileMenu.setTitle(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b", None))
        self.helpMenu.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0440\u0430\u0432\u043a\u0430", None))
        self.editMenu.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0430\u0432\u043a\u0430", None))
    # retranslateUi

