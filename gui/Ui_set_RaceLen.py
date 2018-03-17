# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'defGui/set_RaceLen.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_set_RaceLen(object):
    def setupUi(self, set_RaceLen):
        set_RaceLen.setObjectName("set_RaceLen")
        set_RaceLen.setWindowModality(QtCore.Qt.ApplicationModal)
        set_RaceLen.resize(275, 82)
        set_RaceLen.setWindowTitle("")
        set_RaceLen.setLocale(QtCore.QLocale(QtCore.QLocale.French, QtCore.QLocale.Switzerland))
        set_RaceLen.setModal(True)
        self.buttonBox = QtWidgets.QDialogButtonBox(set_RaceLen)
        self.buttonBox.setGeometry(QtCore.QRect(180, 10, 81, 301))
        self.buttonBox.setToolTip("")
        self.buttonBox.setStatusTip("")
        self.buttonBox.setAccessibleName("")
        self.buttonBox.setAccessibleDescription("")
        self.buttonBox.setLocale(QtCore.QLocale(QtCore.QLocale.French, QtCore.QLocale.Switzerland))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayoutWidget = QtWidgets.QWidget(set_RaceLen)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 10, 175, 88))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.durELabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.durELabel.setToolTip("")
        self.durELabel.setStatusTip("")
        self.durELabel.setAccessibleName("")
        self.durELabel.setAccessibleDescription("")
        self.durELabel.setLocale(QtCore.QLocale(QtCore.QLocale.French, QtCore.QLocale.Switzerland))
        self.durELabel.setObjectName("durELabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.durELabel)
        self.durETimeEdit = QtWidgets.QTimeEdit(self.formLayoutWidget)
        self.durETimeEdit.setToolTip("")
        self.durETimeEdit.setStatusTip("")
        self.durETimeEdit.setAccessibleName("")
        self.durETimeEdit.setAccessibleDescription("")
        self.durETimeEdit.setLocale(QtCore.QLocale(QtCore.QLocale.French, QtCore.QLocale.Switzerland))
        self.durETimeEdit.setMinimumDate(QtCore.QDate(2000, 3, 31))
        self.durETimeEdit.setCurrentSection(QtWidgets.QDateTimeEdit.MinuteSection)
        self.durETimeEdit.setDisplayFormat("hh:mm")
        self.durETimeEdit.setTimeSpec(QtCore.Qt.UTC)
        self.durETimeEdit.setTime(QtCore.QTime(0, 10, 0))
        self.durETimeEdit.setObjectName("durETimeEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.durETimeEdit)
        self.nbTourLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.nbTourLabel.setObjectName("nbTourLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.nbTourLabel)
        self.nbTourIntNumInput = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.nbTourIntNumInput.setToolTip("")
        self.nbTourIntNumInput.setStatusTip("")
        self.nbTourIntNumInput.setAccessibleName("")
        self.nbTourIntNumInput.setAccessibleDescription("")
        self.nbTourIntNumInput.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhPreferNumbers)
        self.nbTourIntNumInput.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.nbTourIntNumInput.setSpecialValueText("")
        self.nbTourIntNumInput.setSuffix(" Tour(s)")
        self.nbTourIntNumInput.setObjectName("nbTourIntNumInput")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.nbTourIntNumInput)

        self.retranslateUi(set_RaceLen)
        self.buttonBox.accepted.connect(set_RaceLen.accept)
        self.buttonBox.rejected.connect(set_RaceLen.reject)
        QtCore.QMetaObject.connectSlotsByName(set_RaceLen)

    def retranslateUi(self, set_RaceLen):
        _translate = QtCore.QCoreApplication.translate
        self.durELabel.setText(_translate("set_RaceLen", "Durée"))
        self.nbTourLabel.setText(_translate("set_RaceLen", "Nb Tour"))

