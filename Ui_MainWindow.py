# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.French, QtCore.QLocale.Switzerland))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 800, 560))
        self.tabWidget.setMinimumSize(QtCore.QSize(800, 260))
        self.tabWidget.setMaximumSize(QtCore.QSize(800, 560))
        self.tabWidget.setObjectName("tabWidget")
        self.Tab_Racer = QtWidgets.QWidget()
        self.Tab_Racer.setToolTip("")
        self.Tab_Racer.setAccessibleName("")
        self.Tab_Racer.setObjectName("Tab_Racer")
        self.scrollArea = QtWidgets.QScrollArea(self.Tab_Racer)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 261, 531))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 259, 529))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.L_racerlist = QtWidgets.QListWidget(self.scrollAreaWidgetContents)
        self.L_racerlist.setGeometry(QtCore.QRect(0, 0, 256, 491))
        font = QtGui.QFont()
        font.setFamily("Bitstream Charter")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(False)
        self.L_racerlist.setFont(font)
        self.L_racerlist.setMouseTracking(True)
        self.L_racerlist.setAcceptDrops(True)
        self.L_racerlist.setStyleSheet("font: 10pt \"Bitstream Charter\";")
        self.L_racerlist.setInputMethodHints(QtCore.Qt.ImhPreferLatin)
        self.L_racerlist.setDefaultDropAction(QtCore.Qt.CopyAction)
        self.L_racerlist.setProperty("isWrapping", False)
        self.L_racerlist.setViewMode(QtWidgets.QListView.ListMode)
        self.L_racerlist.setModelColumn(0)
        self.L_racerlist.setObjectName("L_racerlist")
        self.gridLayoutWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 490, 261, 41))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(6, 0, 6, 0)
        self.gridLayout.setHorizontalSpacing(4)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.toolButton = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.toolButton.setObjectName("toolButton")
        self.gridLayout.addWidget(self.toolButton, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setEnabled(True)
        self.label_2.setMaximumSize(QtCore.QSize(80, 60))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_2.setFont(font)
        self.label_2.setToolTip("")
        self.label_2.setStatusTip("")
        self.label_2.setAccessibleName("")
        self.label_2.setAccessibleDescription("")
        self.label_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.findNumber = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.findNumber.setMaximumSize(QtCore.QSize(100, 60))
        font = QtGui.QFont()
        font.setKerning(True)
        self.findNumber.setFont(font)
        self.findNumber.setMouseTracking(True)
        self.findNumber.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.findNumber.setAcceptDrops(False)
        self.findNumber.setToolTip("")
        self.findNumber.setStatusTip("")
        self.findNumber.setAccessibleName("")
        self.findNumber.setAccessibleDescription("")
        self.findNumber.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.findNumber.setInputMask("")
        self.findNumber.setText("")
        self.findNumber.setMaxLength(5)
        self.findNumber.setPlaceholderText("")
        self.findNumber.setObjectName("findNumber")
        self.horizontalLayout.addWidget(self.findNumber)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.formLayoutWidget = QtWidgets.QWidget(self.Tab_Racer)
        self.formLayoutWidget.setGeometry(QtCore.QRect(260, 0, 531, 521))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setVerticalSpacing(2)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.R_lastname = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.R_lastname.setObjectName("R_lastname")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.R_lastname)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.R_firstname = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.R_firstname.setObjectName("R_firstname")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.R_firstname)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.R_number = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.R_number.setToolTip("")
        self.R_number.setStatusTip("")
        self.R_number.setAccessibleName("")
        self.R_number.setAccessibleDescription("")
        self.R_number.setInputMethodHints(QtCore.Qt.ImhDialableCharactersOnly|QtCore.Qt.ImhDigitsOnly)
        self.R_number.setText("00000")
        self.R_number.setMaxLength(5)
        self.R_number.setObjectName("R_number")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.R_number)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.R_transponder = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.R_transponder.setToolTip("")
        self.R_transponder.setStatusTip("")
        self.R_transponder.setAccessibleName("")
        self.R_transponder.setAccessibleDescription("")
        self.R_transponder.setInputMethodHints(QtCore.Qt.ImhDialableCharactersOnly|QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhFormattedNumbersOnly)
        self.R_transponder.setText("0000000000")
        self.R_transponder.setMaxLength(12)
        self.R_transponder.setObjectName("R_transponder")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.R_transponder)
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.R_city = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.R_city.setObjectName("R_city")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.R_city)
        self.label_11 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.R_brand = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.R_brand.setMouseTracking(False)
        self.R_brand.setAcceptDrops(False)
        self.R_brand.setStatusTip("")
        self.R_brand.setAccessibleName("")
        self.R_brand.setAccessibleDescription("")
        self.R_brand.setInputMask("")
        self.R_brand.setText("Marque Moto")
        self.R_brand.setPlaceholderText("")
        self.R_brand.setObjectName("R_brand")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.R_brand)
        self.label_12 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_12.setObjectName("label_12")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_12)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(11, QtWidgets.QFormLayout.SpanningRole, spacerItem)
        self.R_brandMenu = QtWidgets.QComboBox(self.formLayoutWidget)
        self.R_brandMenu.setToolTip("")
        self.R_brandMenu.setStatusTip("")
        self.R_brandMenu.setAccessibleName("")
        self.R_brandMenu.setAccessibleDescription("")
        self.R_brandMenu.setEditable(False)
        self.R_brandMenu.setCurrentText("TM Racing")
        self.R_brandMenu.setObjectName("R_brandMenu")
        self.R_brandMenu.addItem("")
        self.R_brandMenu.setItemText(0, "TM Racing")
        self.R_brandMenu.addItem("")
        self.R_brandMenu.setItemText(1, "Yamaha")
        self.R_brandMenu.addItem("")
        self.R_brandMenu.setItemText(2, "Honda")
        self.R_brandMenu.addItem("")
        self.R_brandMenu.setItemText(3, "Suzuki")
        self.R_brandMenu.addItem("")
        self.R_brandMenu.setItemText(4, "Citrouille Pourrie")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.R_brandMenu)
        self.R_Categorie = QtWidgets.QTreeWidget(self.formLayoutWidget)
        self.R_Categorie.setToolTip("")
        self.R_Categorie.setStatusTip("")
        self.R_Categorie.setAccessibleName("")
        self.R_Categorie.setAccessibleDescription("")
        self.R_Categorie.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.R_Categorie.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.R_Categorie.setHeaderHidden(False)
        self.R_Categorie.setExpandsOnDoubleClick(True)
        self.R_Categorie.setObjectName("R_Categorie")
        item_0 = QtWidgets.QTreeWidgetItem(self.R_Categorie)
        self.R_Categorie.topLevelItem(0).setText(0, "MX1")
        item_0.setToolTip(0, "")
        item_0.setStatusTip(0, "")
        item_0.setCheckState(0, QtCore.Qt.Unchecked)
        item_0.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.R_Categorie.topLevelItem(0).child(0).setText(0, "Top")
        item_1.setToolTip(0, "")
        item_1.setStatusTip(0, "")
        item_1.setWhatsThis(0, "")
        item_1.setCheckState(0, QtCore.Qt.Unchecked)
        item_1.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.R_Categorie.topLevelItem(0).child(1).setText(0, "Pro")
        item_1.setToolTip(0, "")
        item_1.setStatusTip(0, "")
        item_1.setWhatsThis(0, "")
        item_1.setCheckState(0, QtCore.Qt.Unchecked)
        item_1.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.R_Categorie.topLevelItem(0).child(2).setText(0, "Cartons")
        item_1.setToolTip(0, "")
        item_1.setStatusTip(0, "")
        item_1.setWhatsThis(0, "")
        item_1.setCheckState(0, QtCore.Qt.Unchecked)
        item_1.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        item_0 = QtWidgets.QTreeWidgetItem(self.R_Categorie)
        self.R_Categorie.topLevelItem(1).setText(0, "Mini")
        item_0.setToolTip(0, "")
        item_0.setStatusTip(0, "")
        item_0.setWhatsThis(0, "")
        item_0.setCheckState(0, QtCore.Qt.Unchecked)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.R_Categorie.topLevelItem(1).child(0).setText(0, "Mini")
        item_1.setToolTip(0, "")
        item_1.setStatusTip(0, "")
        item_1.setCheckState(0, QtCore.Qt.Unchecked)
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.R_Categorie)
        self.R_date = QtWidgets.QDateEdit(self.formLayoutWidget)
        self.R_date.setInputMethodHints(QtCore.Qt.ImhDate|QtCore.Qt.ImhPreferNumbers)
        self.R_date.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(7918, 1, 1), QtCore.QTime(23, 59, 59)))
        self.R_date.setMaximumDate(QtCore.QDate(7918, 1, 1))
        self.R_date.setCalendarPopup(True)
        self.R_date.setObjectName("R_date")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.R_date)
        self.tabWidget.addTab(self.Tab_Racer, "")
        self.Tab_race = QtWidgets.QWidget()
        self.Tab_race.setObjectName("Tab_race")
        self.tabWidget.addTab(self.Tab_race, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 19))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.menuFfff = QtWidgets.QMenu(self.menubar)
        self.menuFfff.setObjectName("menuFfff")
        self.menuConcurrents = QtWidgets.QMenu(self.menubar)
        self.menuConcurrents.setObjectName("menuConcurrents")
        self.menuCourses = QtWidgets.QMenu(self.menubar)
        self.menuCourses.setObjectName("menuCourses")
        self.menuR_sultats = QtWidgets.QMenu(self.menubar)
        self.menuR_sultats.setObjectName("menuR_sultats")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuitter = QtWidgets.QAction(MainWindow)
        self.actionQuitter.setShortcut("Ctrl+Q")
        self.actionQuitter.setMenuRole(QtWidgets.QAction.QuitRole)
        self.actionQuitter.setObjectName("actionQuitter")
        self.actionNouvelle_Course = QtWidgets.QAction(MainWindow)
        self.actionNouvelle_Course.setObjectName("actionNouvelle_Course")
        self.actionOuvrire = QtWidgets.QAction(MainWindow)
        self.actionOuvrire.setObjectName("actionOuvrire")
        self.actionEnregister = QtWidgets.QAction(MainWindow)
        self.actionEnregister.setObjectName("actionEnregister")
        self.actionEnregistrer_Sous = QtWidgets.QAction(MainWindow)
        self.actionEnregistrer_Sous.setObjectName("actionEnregistrer_Sous")
        self.menuFfff.addSeparator()
        self.menuFfff.addSeparator()
        self.menuFfff.addAction(self.actionNouvelle_Course)
        self.menuFfff.addAction(self.actionOuvrire)
        self.menuFfff.addAction(self.actionEnregister)
        self.menuFfff.addAction(self.actionEnregistrer_Sous)
        self.menuFfff.addSeparator()
        self.menuFfff.addAction(self.actionQuitter)
        self.menubar.addAction(self.menuFfff.menuAction())
        self.menubar.addAction(self.menuConcurrents.menuAction())
        self.menubar.addAction(self.menuCourses.menuAction())
        self.menubar.addAction(self.menuR_sultats.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RaceChrono (c) Yves Huguenin 2018"))
        self.toolButton.setText(_translate("MainWindow", "Ajouter"))
        self.label_2.setText(_translate("MainWindow", "Numéro:"))
        self.pushButton.setText(_translate("MainWindow", "Effacer"))
        self.label.setText(_translate("MainWindow", "Nom"))
        self.R_lastname.setText(_translate("MainWindow", "R_LastName"))
        self.label_6.setText(_translate("MainWindow", "Prénom"))
        self.R_firstname.setText(_translate("MainWindow", "R_FirstName"))
        self.label_8.setText(_translate("MainWindow", "Numéro course"))
        self.label_7.setText(_translate("MainWindow", "Transpondeur"))
        self.label_9.setText(_translate("MainWindow", "Catégorie"))
        self.label_10.setText(_translate("MainWindow", "Localité"))
        self.R_city.setText(_translate("MainWindow", "R_Localité"))
        self.label_11.setText(_translate("MainWindow", "Marque"))
        self.label_12.setText(_translate("MainWindow", "Date naissance"))
        self.R_Categorie.setSortingEnabled(True)
        self.R_Categorie.headerItem().setText(0, _translate("MainWindow", "Catégories"))
        __sortingEnabled = self.R_Categorie.isSortingEnabled()
        self.R_Categorie.setSortingEnabled(False)
        self.R_Categorie.setSortingEnabled(__sortingEnabled)
        self.R_date.setDisplayFormat(_translate("MainWindow", "dd MMMM yyyy"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Tab_Racer), _translate("MainWindow", "Concurrents"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Tab_race), _translate("MainWindow", "Courses"))
        self.menuFfff.setTitle(_translate("MainWindow", "Fichier"))
        self.menuConcurrents.setTitle(_translate("MainWindow", "&Concurrents"))
        self.menuCourses.setTitle(_translate("MainWindow", "Co&urses"))
        self.menuR_sultats.setTitle(_translate("MainWindow", "R&ésultats"))
        self.actionQuitter.setText(_translate("MainWindow", "&Quitter"))
        self.actionQuitter.setWhatsThis(_translate("MainWindow", "Quit le programme"))
        self.actionNouvelle_Course.setText(_translate("MainWindow", "&Nouvelle Course"))
        self.actionOuvrire.setText(_translate("MainWindow", "&Ouvrire"))
        self.actionEnregister.setText(_translate("MainWindow", "&Enregister"))
        self.actionEnregistrer_Sous.setText(_translate("MainWindow", "Enregistrer &Sous"))

