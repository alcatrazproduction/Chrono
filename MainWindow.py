#!/usr/bin/python

from PyQt5.QtGui		import	QFont
from PyQt5 				import   QtWidgets, QtCore
from T_Marques		import 	T_Marques
from T_Concurrents	import 	T_Concurrents
from Ui_MainWindow	import Ui_MainWindow

import	Globals

racer = [
#	[66,'SCHAFER',"Alain","Fribourg","Honda"],
#	[906,"CORTIJO","Yohan","Illarsaz","Yamaha"],
#	[28,"POGET","Elies","Echandens","KTM"],
#	[718,"YERLY","Cedric","Treyvaux","Kawasaki"],
#	[819,"WENGER","Marc","Alterswil","Husqvarna"],
#	[3,"PEISSARD","Patrick","Matran","Kawasaki"],
#	[108,"FAHRNI","Normand","Broc","Suzuki"],
#	[15,"SIMOND","Baptiste","Lovatens","Honda"],
#	[100,"SCHAFER","Samuel","Giffers","Honda"],
#	[94,"AEBERSOLD","Remo","Bleiken","Yamaha"],
#	[11,"FRACHEBOUD","Louis","Puidoux","Yamaha"],
#	[222,"BRODARD","Olivier","Posieux","Honda"],
#	[49,"COUTAZ","Sebastien","Genolier","KTM"],
#	[12,"SCHUPBACH","Valentin","Arconciel","Kawasaki"],
#	[221,"HINNI","Joel","Zollikofen","Yamaha"],
#	[932,"SALLIN","Junior","Belfaux","Kawasaki"],
#	[17,"DA VEIGA","Diego","Vendlincourt","KTM"],
#	[892,"KILCHOER","Loec","La Roche","KTM"],
#	[907,"SALLIN","Louis","Belfaux","KTM"],
#	[32,"SCHUPBACH","David","Arconciel","Kawasaki"],
#	[2,"GUISOLAN","Sven","Noreaz","TM"],
#	[59,"CHAUTEMS","Remy","Chene-Paquier","Suzuki"],
#	[421,"WAEBER","Mathieu","Ecuvillens","Yamaha"],
#	[129,"ZUGER","Neal","Cressier","KTM"]
]

_categorie = [
	["MX1", ["Top", "Pro", "Carton"]],
	["MX2", ["Top", "Pro", "Carton"]],
	["Mini", ["Mini"]],
	["MX125", ["Top", "Pro", "Carton"]],
	["MX3", ["MX3", "Carton"]]
]
UserRole	 = 0x0100

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
	__RacerEdited = None

	def getRacer(self):
		return self.__RacerEdited

	def setRacer(self, theRacer):
		self.__RacerEdited = theRacer

	def __init__(self, parent=None):
		super(MainWindow, self).__init__(parent)
		self.setupUi(self)

	def connectActions(self):
		self.actionQuitter.triggered.connect(QtWidgets.qApp.quit)
		self.L_racerlist.itemDoubleClicked.connect(self.editRacer)
		self.findNumber.returnPressed.connect(self.findNumRacer)

	def findNumRacer(self):
		try:
			fn = int( self.findNumber.text() )
			item = self.L_racerlist.findItems( "%4.0d"%fn,  QtCore.Qt.MatchStartsWith)
		except:
			return
		if len( item )>0:
			self.L_racerlist.setCurrentItem( item[0])
			self.editRacer( item[0] )

	def editRacer(self, item):
		racer = item.data(UserRole)
		print (racer)
		oldracerItem = self.__RacerEdited
		if oldracerItem is not None:
			rl 	= self.R_lastname.text()
			rf	= self.R_firstname.text()
			try:
				rn	= int( self.R_number.text() )
			except:
				rn = 0
			try:
				rt 	= int( self.R_transponder.text() )
			except:
				rt 	= 0
			rm = self.R_brandMenu.itemData( self.R_brandMenu.currentIndex() )
			oldracer			= oldracerItem.data( UserRole )
			if oldracer is None:
				oldracer = [ 0,  "", "",  "", "",  0]

			oldracer['numero']			= rn
			oldracer['nom']					= rl
			oldracer['prenom']			= rf
			oldracer['transponder'] 		= rt
			oldracer['moto']				= rm
			oldracerItem.setText( Globals.C_concurrents_item_fmt %  ( oldracer['numero'],   oldracer['nom'],  oldracer['prenom'] ) )
			oldracerItem.setData( UserRole,  oldracer )

		if racer is None :
			self.R_lastname.setText(		"" )
			self.R_firstname.setText(		"" )
			self.R_number.setText(		"" )
			self.R_transponder.setText(	"")
		else:
			self.R_lastname.setText(		racer['nom'] )
			self.R_firstname.setText(		racer['prenom'] )
			self.R_number.setText(		"%d"%racer['numero'] )
#			if len( racer ) > 5:
			self.R_transponder.setText(	"%d"%racer['transponder'])
#			else:
#				self.R_transponder.setText(	"")
			self.R_brandMenu.setCurrentIndex( self.R_brandMenu.findData(racer['moto']))
			self.__RacerEdited = item


	def main(self):
		self.connectActions()
		self.L_racerlist.setSortingEnabled(True)
		self.concurrents = T_Concurrents()
		while self.concurrents.getNextRecord():
			c = dict( self.concurrents._data )
			c['transponder'] = 0
			racer.append( c )
		font = QFont()
		font.setFamily("Courier New")
		font.setPointSize(8)
		font.setBold(False)
		font.setItalic(False)
		font.setWeight(50)
		font.setKerning(False)
		for i in racer:
			item = QtWidgets.QListWidgetItem()
			item.setText( Globals.C_concurrents_item_fmt %  ( i['numero'],   i['nom'],  i['prenom'] ) )
			item.setData( UserRole, i )
			item.setFont( font )
			self.L_racerlist.addItem(item)
		self.marques = T_Marques()
		self.R_brandMenu.clear()
		while self.marques.getNextRecord():
			c = dict( self.marques._data )
			self.R_brandMenu.addItem(c['nom'], c['id'])
		self.show()
