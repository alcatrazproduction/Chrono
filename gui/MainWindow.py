#!/usr/bin/python3



from PyQt5 			import   	QtWidgets, QtCore
from PyQt5.QtCore		import 	QTimer
from PyQt5.QtGui		import	QBrush
from Ui_MainWindow		import 	Ui_MainWindow
# Tables definition imports
from T_Marques			import 	T_Marques
from T_Concurrents		import 	T_Concurrents
from T_Pays			import 	T_Pays
from T_Ville			import 	T_Ville
import	Globals
from Set_RacerTp		import 	Set_RacerTp

_categorie = [
	["MX1", ["Top", "Pro", "Carton"]],
	["MX2", ["Top", "Pro", "Carton"]],
	["Mini", ["Mini"]],
	["MX125", ["Top", "Pro", "Carton"]],
	["MX3", ["MX3", "Carton"]]
]


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
		self.actionQuitter.triggered.connect(				QtWidgets.qApp.quit )
		self.L_racerlist.itemDoubleClicked.connect(			self.editRacer)
		self.findNumber.returnPressed.connect(				self.findNumRacer)
		self.R_Npa.returnPressed.connect(					self.findNpa)
		self.R_City.returnPressed.connect(					self.findVille)
		self.RB_Add.clicked.connect( 						self.addRacer )
		self.TM_T_passage.itemDoubleClicked.connect(			self.setRacerTb)

	def setRacerTb(self, item):
		row 	= self.TM_T_passage.currentRow()
		dlg 	= Set_RacerTp()
		dlg.main()
		if dlg.exec_():
			if dlg.getDict() == None:
				return
			d = dlg.getDict()
			tp = int( self.TM_T_passage.item(row, 2).text() )
			d['transponder'] = tp
			Globals.tpRacerList[ Globals.C_concurrents_TP_fmt%tp]=dlg.r_item.data(Globals.UserRole)

	def addRacer(self):
		item = QtWidgets.QListWidgetItem()
		item.setText( "Nouveau" )
		self.concurrents.newRecord()
		c = dict( self.concurrents._data )
		c['transponder'] = 0
		item.setData( Globals.UserRole, c )
		item.setFont( Globals.C_listFont )
		self.L_racerlist.addItem(item)
		self.editRacer( item )
		title = "%s (%d)"%(QtCore.QCoreApplication.translate("MainWindow", "Concurrents"), self.L_racerlist.count())
		self.Tab_Container.setTabText(self.Tab_Container.indexOf(self.T_Racer), title)
		Globals.racerList[ Globals.C_concurrents_ID_fmt%( len(Globals.racerList)+10001 )] = c

	def findNpa(self):
		try:
			fn = self.R_Npa.text()
			pa	= self.R_Pays.itemData( self.R_Pays.currentIndex() )
			if self.t_ville.getRecord( "npa LIKE '%s' AND pays LIKE '%s'"%(fn , pa )):
				c = dict( self.t_ville._data )
				self.R_City.setText( c['nom'] )
				self.R_Npa.setText( c['npa']  )
		except Exception as e:
			print(e)
			return

	def findVille(self):
		try:
			fn = self.R_City.text()
			pa	= self.R_Pays.itemData( self.R_Pays.currentIndex() )
			if self.t_ville.getRecord( "nom LIKE '%s' AND pays LIKE '%s'"%(fn , pa )):
				c = dict( self.t_ville._data )
				self.R_Npa.setText( c['npa']  )
				self.R_City.setText( c['nom'] )
			elif self.t_ville.getRecord( "nom LIKE '%s%c' AND pays LIKE '%s'"%(fn ,'%', pa )):
				c = dict( self.t_ville._data )
				self.R_Npa.setText( c['npa']  )
				self.R_City.setText( c['nom'] )
		except Exception as e:
			print(e)
			return

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
		id = item.data(Globals.UserRole)
		print (id)
		racer = Globals.racerList[ id]
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
			rp	= self.R_Npa.text()
			rc	= self.R_City.text()
			pa	= self.R_Pays.itemData( self.R_Pays.currentIndex() )
			oldracer			=  Globals.racerList[ oldracerItem.data( Globals.UserRole )]
			if oldracer is None:
				oldracer = [ ]

			oldracer['numero']				= rn
			oldracer['nom']				= rl
			oldracer['prenom']				= rf
			if oldracer['transponder'] != rt:
				if Globals.C_concurrents_TP_fmt%oldracer['transponder'] in Globals.tpRacerList:
					Globals.tpRacerList.pop( Globals.C_concurrents_TP_fmt%oldracer['transponder'] )
				oldracer['transponder'] 		= rt
				Globals.tpRacerList[ Globals.C_concurrents_TP_fmt%rt ] = oldracerItem.data( Globals.UserRole )

			oldracer['moto']				= rm
			oldracer['ville']				= rc
			oldracer['npa']				= rp
			oldracer['pays']				= pa
			oldracerItem.setText( Globals.C_concurrents_item_fmt %  ( oldracer['numero'],   oldracer['nom'],  oldracer['prenom'] ) )

		if racer is None :
			self.R_lastname.setText(			"" )
			self.R_firstname.setText(		"" )
			self.R_number.setText(			"" )
			self.R_transponder.setText(		"")
		else:
			self.R_lastname.setText(			racer['nom'] )
			self.R_firstname.setText(		racer['prenom'] )
			self.R_number.setText(		"%d"%racer['numero'] )
			self.R_transponder.setText(	"%d"%racer['transponder'])
			self.R_brandMenu.setCurrentIndex( self.R_brandMenu.findData(racer['moto']))
			pa 							= racer['pays']
			if pa == None:
				pa = 'CHE'
			self.R_Pays.setCurrentIndex( self.R_Pays.findData( pa ))
			self.__RacerEdited = item
			self.R_Npa.setText(				racer['npa'])
			self.R_City.setText(			racer['ville'])
			if racer['npa'] == None:
				self.findVille()
			if racer['ville'] == None:
				self.findNpa()

	def initGuiPays(self):
		self.pays = T_Pays()
		self.R_Pays.clear()
		i = 0
		while self.pays.getRecord("display = TRUE", i):
			c = dict( self.pays._data )
			self.R_Pays.addItem(c['nom'], c['id'])
			i += 1

	def initGuiMarques(self):
		self.marques = T_Marques()
		self.R_brandMenu.clear()
		while self.marques.getNextRecord():
			c = dict( self.marques._data )
			self.R_brandMenu.addItem(c['nom'], c['id'])

	def initListConcurrents(self):
		self.L_racerlist.setSortingEnabled(True)
		self.concurrents = T_Concurrents()
		while self.concurrents.getNextRecord():
			c = dict( self.concurrents._data )
			c['transponder'] = 0
			Globals.racerList[ Globals.C_concurrents_ID_fmt%( c['id'] )] = c

	def initGuiConcurrents(self):
		for id in Globals.racerList:
			i = Globals.racerList[id]
			item = QtWidgets.QListWidgetItem()
			item.setText( Globals.C_concurrents_item_fmt %  ( i['numero'],   i['nom'],  i['prenom'] ) )
			item.setData( Globals.UserRole, id)
			item.setFont( Globals.C_listFont )
			self.L_racerlist.addItem(item)
		title = "%s (%d)"%(QtCore.QCoreApplication.translate("MainWindow", "Concurrents"), self.L_racerlist.count())
		self.Tab_Container.setTabText(self.Tab_Container.indexOf(self.T_Racer), title)

	def initGui(self):
		self.t_ville = T_Ville()
		self.initGuiPays()
		self.initGuiMarques()
		self.initListConcurrents()
		self.initGuiConcurrents()

	def updateMonitor(self):
		def setLine(self, color, row, column, text):
			brush = QBrush(color)
			brush.setStyle(QtCore.Qt.SolidPattern)
			i = QtWidgets.QTableWidgetItem( text )
			i.setBackground( brush )
			self.TM_T_passage.setItem(row, column, i )

		for task in Globals.receiver:
			print( task )
			t = Globals.receiver[task].task
			for r in t:
				print (r)
				q = t[r]['queue']['monitor']
				print( q )
				print("***********************************************************")
				while not q.empty():
					e = q.get_nowait()
					tp = e.tp
					millis = e.millis
					c=Globals.colorWhite
					try:
						if tp in Globals.dictBestLapMonitor:
							tt = Globals.dictBestLapMonitor[tp]
							if tt['ridernum']== 0:
								if "TP_%8.8X"%tp in Globals.tpRacerList :
									c	= Globals.racerList[ Globals.tpRacerList[ Globals.C_concurrents_TP_fmt%tp ] ]
									tt['ridername']	= Globals.C_concurrents_moni_fmt%(c['nom'], c['prenom'])	# I_ridername
									tt['ridernum']		= c['numero']										# I_ridernum

							lap		= millis - tt['lasttick']
							tt['lasttick' ] = millis
							tt['lastlap']	= lap
							if lap < tt['bestlap']:
								tt['bestlap'] = lap
								tt['textcolor'] = Globals.text_inverted + Globals.text_green
								c = Globals.colorGreen
							if lap > tt['bestlap']:
								tt['textcolor'] = Globals.text_inverted + Globals.text_red
								c = Globals.colorRed
							tt['lapcount']+=1
							tt['updated']	= True
						else:
								Globals.dictBestLapMonitor[tp] = dict()
								tt = Globals.dictBestLapMonitor[tp]
								tt['bestlap']	=Globals.max_time 									# I_bestlap
								tt['lastlap'] 	=0 														# I_lastlap
								if "TP_%8.8X"%tp in Globals.tpRacerList :
									c	= Globals.racerList[ Globals.tpRacerList[ Globals.C_concurrents_TP_fmt%tp ] ]
									tt['ridername']		= c['nom']							# I_ridername
									tt['ridernum']		= c['numero']						# I_ridernum
								else:
									tt['ridername']		=""
									tt['ridernum']		= 0
								tt['lasttick']		= millis												# I_lasttick
								tt['lapcount']		= 0 													# I_lapcount
								tt['totticks']		= 0.999999999 									# I_totticks
								tt['updated']		= True												# I_updated
								tt['textcolor']		= Globals.text_inverted + Globals.text_blue	# I_textcolor
								c = Globals.colorBlue
						self.TM_T_passage.setSortingEnabled(False)
						r		= self.TM_T_passage.rowCount()
						if r > 40:
							self.TM_T_passage.removeRow(0)
							r = 40
						self.TM_T_passage.insertRow( r )
						self.TM_T_passage.setRowHeight( r,  12)

						setLine( self, c, r,  0,task)
						setLine( self, c, r,  1, Globals.createTime(millis ) )
						setLine( self, c, r,  2, "%8d"%tp )
						setLine( self, c, r,  3,Globals.createTime(tt['lastlap'] ) )

						if tt['ridernum'] == 0:
							brush = QBrush(Globals.colorCyan)
							brush.setStyle(QtCore.Qt.SolidPattern)
							i = QtWidgets.QTableWidgetItem("")
							i.setBackground( brush )
							self.TM_T_passage.setItem(r, 4, i )
							i = QtWidgets.QTableWidgetItem("")
							i.setBackground( brush )
							self.TM_T_passage.setItem(r, 5, i )
						else:
							self.TM_T_passage.setItem(r, 4, QtWidgets.QTableWidgetItem("%5d"%tt['ridernum']))
							self.TM_T_passage.setItem(r, 5, QtWidgets.QTableWidgetItem(tt['ridername']))

					except  Exception as e:
						print("in updateNonitor")
						print( e )

	def main(self):
		self.connectActions()
		self.initGui()
		self.timer = QTimer()
		self.timer.timeout.connect(self.updateMonitor)
		self.timer.start(1000)
		self.show()
