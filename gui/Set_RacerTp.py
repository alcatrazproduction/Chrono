#!/usr/bin/python
######################################################################################
# (c) Yves Huguenin, yves.huguenin@free.fr, mars 2018							#
######################################################################################

from PyQt5 				import   QtWidgets, QtCore
from Ui_Set_RacerTp	import Ui_Set_RacerTp
# Tables definition imports
#from T_Marques		import 	T_Marques
#from T_Concurrents	import 	T_Concurrents
#from T_Pays			import 	T_Pays
#from T_Ville				import 	T_Ville
import	Globals

class Set_RacerTp(QtWidgets.QDialog, Ui_Set_RacerTp):
	def __init__(self, parent=None):
		self.r_num		= None
		self.r_fname		= None
		self.r_lname		= None
		self.r_dict		= None
		self.r_item		= None
		self.r_index		= None

		super(Set_RacerTp, self).__init__(parent)
		self.setupUi(self)
	def getNum(self):
		return self.r_num

	def getFname(self):
		return self.r_fname

	def getLname(self):
			return self.r_lname

	def getDict(self):
		return self.r_dict

	def main(self):
		self.connectActions()
		self.initGui()
		self.show()

	def initGui(self):
		print()

	def findNumRacer(self):
		try:
			fn = int( self.R_number.text() )
			item = Globals.MainWindow.L_racerlist.findItems( "%4.0d"%fn,  QtCore.Qt.MatchStartsWith)
		except:
			return
		if len( item )>0:
			d						=  Globals.racerList[ item[0].data(Globals.UserRole) ]
			self.r_item			=  item[0]
			self.R_firstname.setText( d['prenom'] )
			self.R_lastname.setText( d['nom'] )
			self.r_num			= fn
			self.r_fname			= d['prenom']
			self.r_lname			= d['nom']
			self.r_dict			= d
			self.OkBtn.setEnabled(True)
		else:
			self.OkBtn.setEnabled(False)

	def connectActions(self):
		self.R_number.returnPressed.connect(self.findNumRacer)

# Globals.MainWindow
