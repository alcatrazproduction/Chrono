#!/usr/bin/python

from PyQt5 				import   QtWidgets, QtCore
from PyQt5.QtCore	import QTimer
from Ui_Set_RacerTp	import Ui_Set_RacerTp
# Tables definition imports
#from T_Marques		import 	T_Marques
#from T_Concurrents	import 	T_Concurrents
#from T_Pays			import 	T_Pays
#from T_Ville				import 	T_Ville
import	Globals

class Set_RacerTp(QtWidgets.QMainWindow, Ui_Set_RacerTp):
	def __init__(self, parent=None):
		super(Set_RacerTp, self).__init__(parent)
		self.setupUi(self)

	def main(self):
		self.connectActions()
		self.initGui()
		self.show()

	def initGui(self):
		print()

	def connectActions(self):
#		self.actionQuitter.triggered.connect(QtWidgets.qApp.quit)
		print()

