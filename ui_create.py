# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_create.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLabel, QLineEdit, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_createDialog(object):
    def setupUi(self, createDialog):
        if not createDialog.objectName():
            createDialog.setObjectName(u"createDialog")
        createDialog.resize(400, 150)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(createDialog.sizePolicy().hasHeightForWidth())
        createDialog.setSizePolicy(sizePolicy)
        createDialog.setMinimumSize(QSize(400, 150))
        createDialog.setMaximumSize(QSize(400, 150))
        createDialog.setSizeGripEnabled(False)
        createDialog.setModal(True)
        self.verticalLayout_2 = QVBoxLayout(createDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(createDialog)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.lineWidth = QLineEdit(createDialog)
        self.lineWidth.setObjectName(u"lineWidth")
        self.lineWidth.setInputMethodHints(Qt.ImhDigitsOnly)

        self.verticalLayout_2.addWidget(self.lineWidth)

        self.label = QLabel(createDialog)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.lineHeight = QLineEdit(createDialog)
        self.lineHeight.setObjectName(u"lineHeight")
        self.lineHeight.setInputMethodHints(Qt.ImhDigitsOnly)

        self.verticalLayout_2.addWidget(self.lineHeight)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.buttonBox = QDialogButtonBox(createDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout_2.addWidget(self.buttonBox)


        self.retranslateUi(createDialog)
        self.buttonBox.accepted.connect(createDialog.accept)
        self.buttonBox.rejected.connect(createDialog.reject)

        QMetaObject.connectSlotsByName(createDialog)
    # setupUi

    def retranslateUi(self, createDialog):
        createDialog.setWindowTitle(QCoreApplication.translate("createDialog", u"\u041d\u043e\u0432\u043e\u0435 \u043f\u043e\u043b\u0435", None))
        self.label_2.setText(QCoreApplication.translate("createDialog", u"\u0428\u0438\u0440\u0438\u043d\u0430:", None))
        self.lineWidth.setPlaceholderText(QCoreApplication.translate("createDialog", u"0", None))
        self.label.setText(QCoreApplication.translate("createDialog", u"\u0412\u044b\u0441\u043e\u0442\u0430:", None))
        self.lineHeight.setPlaceholderText(QCoreApplication.translate("createDialog", u"0", None))
    # retranslateUi

