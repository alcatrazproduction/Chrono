# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Set_RacerTp.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Set_RacerTp(object):
    def setupUi(self, Set_RacerTp):
        Set_RacerTp.setObjectName("Set_RacerTp")
        Set_RacerTp.resize(419, 114)
        Set_RacerTp.setToolTip("")
        Set_RacerTp.setAccessibleName("")
        Set_RacerTp.setAccessibleDescription("")
        Set_RacerTp.setModal(True)
        self.R_firstname = QtWidgets.QLineEdit(Set_RacerTp)
        self.R_firstname.setEnabled(True)
        self.R_firstname.setGeometry(QtCore.QRect(110, 32, 200, 23))
        self.R_firstname.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setKerning(False)
        self.R_firstname.setFont(font)
        self.R_firstname.setMouseTracking(False)
        self.R_firstname.setAcceptDrops(False)
        self.R_firstname.setToolTip("")
        self.R_firstname.setAccessibleName("")
        self.R_firstname.setAccessibleDescription("")
        self.R_firstname.setInputMask("")
        self.R_firstname.setText("")
        self.R_firstname.setFrame(False)
        self.R_firstname.setReadOnly(True)
        self.R_firstname.setPlaceholderText("")
        self.R_firstname.setObjectName("R_firstname")
        self.label_8 = QtWidgets.QLabel(Set_RacerTp)
        self.label_8.setGeometry(QtCore.QRect(5, 70, 99, 23))
        self.label_8.setObjectName("label_8")
        self.label_6 = QtWidgets.QLabel(Set_RacerTp)
        self.label_6.setGeometry(QtCore.QRect(5, 32, 50, 23))
        self.label_6.setObjectName("label_6")
        self.label = QtWidgets.QLabel(Set_RacerTp)
        self.label.setGeometry(QtCore.QRect(5, 7, 31, 23))
        self.label.setObjectName("label")
        self.R_lastname = QtWidgets.QLineEdit(Set_RacerTp)
        self.R_lastname.setGeometry(QtCore.QRect(110, 7, 201, 23))
        self.R_lastname.setMinimumSize(QtCore.QSize(200, 0))
        self.R_lastname.setMouseTracking(False)
        self.R_lastname.setAcceptDrops(False)
        self.R_lastname.setToolTip("")
        self.R_lastname.setAccessibleName("")
        self.R_lastname.setAccessibleDescription("")
        self.R_lastname.setInputMask("")
        self.R_lastname.setText("")
        self.R_lastname.setFrame(False)
        self.R_lastname.setReadOnly(True)
        self.R_lastname.setPlaceholderText("")
        self.R_lastname.setObjectName("R_lastname")
        self.R_number = QtWidgets.QLineEdit(Set_RacerTp)
        self.R_number.setGeometry(QtCore.QRect(110, 70, 125, 23))
        self.R_number.setToolTip("")
        self.R_number.setStatusTip("")
        self.R_number.setAccessibleName("")
        self.R_number.setAccessibleDescription("")
        self.R_number.setInputMethodHints(QtCore.Qt.ImhDialableCharactersOnly|QtCore.Qt.ImhDigitsOnly)
        self.R_number.setText("")
        self.R_number.setMaxLength(5)
        self.R_number.setObjectName("R_number")
        self.verticalLayoutWidget = QtWidgets.QWidget(Set_RacerTp)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(320, 10, 91, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.OkBtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.OkBtn.setEnabled(False)
        self.OkBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.OkBtn.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.OkBtn.setToolTip("")
        self.OkBtn.setStatusTip("")
        self.OkBtn.setAccessibleName("")
        self.OkBtn.setAccessibleDescription("")
        self.OkBtn.setShortcut("")
        self.OkBtn.setAutoDefault(False)
        self.OkBtn.setObjectName("OkBtn")
        self.verticalLayout.addWidget(self.OkBtn)
        self.CancelBtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.CancelBtn.setToolTip("")
        self.CancelBtn.setStatusTip("")
        self.CancelBtn.setAccessibleName("")
        self.CancelBtn.setAccessibleDescription("")
        self.CancelBtn.setShortcut("")
        self.CancelBtn.setAutoDefault(False)
        self.CancelBtn.setObjectName("CancelBtn")
        self.verticalLayout.addWidget(self.CancelBtn)

        self.retranslateUi(Set_RacerTp)
        self.OkBtn.clicked.connect(Set_RacerTp.accept)
        self.CancelBtn.clicked.connect(Set_RacerTp.reject)
        QtCore.QMetaObject.connectSlotsByName(Set_RacerTp)

    def retranslateUi(self, Set_RacerTp):
        _translate = QtCore.QCoreApplication.translate
        Set_RacerTp.setWindowTitle(_translate("Set_RacerTp", "Dialog"))
        self.label_8.setText(_translate("Set_RacerTp", "Numéro course"))
        self.label_6.setText(_translate("Set_RacerTp", "Prénom"))
        self.label.setText(_translate("Set_RacerTp", "Nom"))
        self.OkBtn.setText(_translate("Set_RacerTp", "Valider"))
        self.CancelBtn.setText(_translate("Set_RacerTp", "Annuler"))
