#!/usr/bin/python

from PyQt5 import   QtWidgets

import Ui_MainWindow
racer = [
	[66,'SCHAFER',"Alain","Fribourg","Honda"],
	[906,"CORTIJO","Yohan","Illarsaz","Yamaha"],
	[28,"POGET","Elies","Echandens","KTM"],
	[718,"YERLY","Cedric","Treyvaux","Kawasaki"],
	[819,"WENGER","Marc","Alterswil","Husqvarna"],
	[3,"PEISSARD","Patrick","Matran","Kawasaki"],
	[108,"FAHRNI","Normand","Broc","Suzuki"],
	[15,"SIMOND","Baptiste","Lovatens","Honda"],
	[100,"SCHAFER","Samuel","Giffers","Honda"],
	[94,"AEBERSOLD","Remo","Bleiken","Yamaha"],
	[11,"FRACHEBOUD","Louis","Puidoux","Yamaha"],
	[222,"BRODARD","Olivier","Posieux","Honda"],
	[49,"COUTAZ","Sebastien","Genolier","KTM"],
	[12,"SCHUPBACH","Valentin","Arconciel","Kawasaki"],
	[221,"HINNI","Joel","Zollikofen","Yamaha"],
	[932,"SALLIN","Junior","Belfaux","Kawasaki"],
	[17,"DA VEIGA","Diego","Vendlincourt","KTM"],
	[892,"KILCHOER","Loec","La Roche","KTM"],
	[907,"SALLIN","Louis","Belfaux","KTM"],
	[32,"SCHUPBACH","David","Arconciel","Kawasaki"],
	[2,"GUISOLAN","Sven","Noreaz","TM"],
	[59,"CHAUTEMS","Remy","Chene-Paquier","Suzuki"],
	[421,"WAEBER","Mathieu","Ecuvillens","Yamaha"],
	[129,"ZUGER","Neal","Cressier","KTM"]
]

_categorie = [
	["MX1", ["Top", "Pro", "Carton"]],
	["MX2", ["Top", "Pro", "Carton"]],
	["Mini", ["Mini"]],
	["MX125", ["Top", "Pro", "Carton"]],
	["MX3", ["MX3", "Carton"]]
]
UserRole	 = 0x0100

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow.Ui_MainWindow):
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

			oldracer			= oldracerItem.data( UserRole )
			if oldracer is None:
				oldracer = [ 0,  "", "",  "", "",  0]

			oldracer[0]	= rn
			oldracer[1]	= rl
			oldracer[2]	= rf
			print (len( oldracer ))
			if len( oldracer ) > 5:
				oldracer[5] = rt
			else:
				oldracer.append( rt )
			oldracerItem.setText("%5.0d, %-15.10s, %-10.10s" %  ( oldracer[0],   oldracer[1],  oldracer[2] ) )
			oldracerItem.setData( UserRole,  oldracer )

		if racer is None :
			self.R_lastname.setText(		"" )
			self.R_firstname.setText(		"" )
			self.R_number.setText(		"" )
			self.R_transponder.setText(	"")
		else:
			self.R_lastname.setText(		racer[1] )
			self.R_firstname.setText(		racer[2] )
			self.R_number.setText(		"%d"%racer[0] )
			if len( racer ) > 5:
				self.R_transponder.setText(	"%d"%racer[5])
			else:
				self.R_transponder.setText(	"")
			self.__RacerEdited = item


	def main(self):
		self.connectActions()
		self.L_racerlist.setSortingEnabled(True)
		for i in racer:
			item = QtWidgets.QListWidgetItem()
			item.setText("%5.0d, %-15.10s, %-10.10s" %  ( i[0],   i[1],  i[2] ) )
			item.setData( UserRole, i )
			self.L_racerlist.addItem(item)
		self.show()
