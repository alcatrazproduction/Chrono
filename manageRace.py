#!/usr/bin/python3 .
######################################################################################
# (c) Yves Huguenin, yves.huguenin@free.fr, mars 2018							#
######################################################################################
from time 			import time
from PyQt5.QtCore		import QTimer, Qt
from PyQt5.QtGui		import QBrush, QIcon
from PyQt5.QtWidgets 	import QTableWidgetItem
from Globals			import receiver, colors, decoder, createTimeSeconds
from Globals			import dictRace, createTime, icons
from queue			import Queue
import Globals

# Column width
char_width	= 7
name_width 	= 26	* char_width
laps_width	= 8	* char_width
time_width	= 12	* char_width

class manageRace():
	cmdStart		= "Start"
	cmdStop		= "Stop"
	cmdSuspend	= "Suspend"
	cmdWaiting	= "Waiting"
	cmdFinish		= "Finish"
	cmdEndTime	= "EndTime"

	_basecol		= 6

	_duration 	= 0
	_laps		= 0
	_status		= ""

	start_time	= 0
	start_time_ms	= 0
	remain_lap	= 0
	partials		= 0
	maxrows		= 0

	def __init__(self, duration, laps, status=cmdWaiting):
		self._duration		= duration
		self._laps		= laps
		self._status		= status
		print("manageRace.__init__(%d, %d, %s)"%(duration, laps,  status))


	def start(self):
		if self._status != self.cmdWaiting:
			return
		self._status		= self.cmdStart
		print( self._status )
		self.start_time_ms	= int( time() * 1000 )
		self.start_time	= int( self.start_time_ms / 1000 )
		self.max_time		= self.start_time + self._duration
		self.remain_lap	= -2
		Globals.MainWindow.B_Stop.setEnabled(True)
		Globals.MainWindow.B_Start.setEnabled(False)
		Globals.MainWindow.R_RaceLive.setColumnCount( self._basecol )
		Globals.MainWindow.R_RaceLive.setColumnHidden(0, True)
		Globals.MainWindow.R_RaceLive.setColumnWidth( 1, name_width)
		Globals.MainWindow.R_RaceLive.setColumnWidth( 2, laps_width)
		Globals.MainWindow.R_RaceLive.setColumnWidth( 3, time_width)
		Globals.MainWindow.R_RaceLive.setColumnWidth( 4, time_width)
		Globals.MainWindow.R_RaceLive.setColumnWidth( 5, time_width)
		Globals.MainWindow.R_RaceLive.setColumnHidden(1, False)
		Globals.MainWindow.R_RaceLive.setColumnHidden(2, False)
		Globals.MainWindow.R_RaceLive.setColumnHidden(3, False)
		Globals.MainWindow.R_RaceLive.setColumnHidden(4, False)
		Globals.MainWindow.R_RaceLive.setColumnHidden(5, False)

		self.maxrows 		= 0
		col 				=  self._basecol
		for task in receiver:
			r = receiver[task]
			r['queue']['race'] = Queue(maxsize=0)
			t = decoder[ task ]['preferences']['type']
			if t != 0:
				if (t + self._basecol ) > col:
					col = t +  self._basecol
					Globals.MainWindow.R_RaceLive.setColumnCount( col )
				item = QTableWidgetItem(task)
				Globals.MainWindow.R_RaceLive.setHorizontalHeaderItem(t + self._basecol-1, item)
				Globals.MainWindow.R_RaceLive.setColumnWidth( t + self._basecol-1, time_width)
		self.partials		= col -  self._basecol
		Globals.MainWindow.PB_TimeRace.setMaximum( self._duration )
		Globals.MainWindow.PB_TimeRace.setProperty("value", 0)

		self.private		= {}
		self.timer 		= QTimer()
		self.timer.timeout.connect(self.update)
		self.timer.start(1000)


	def update(self):
		def setLine( color, row, column, text, icon = None):
			try:
				brush = QBrush(color)
				brush.setStyle(Qt.SolidPattern)
				i = Globals.MainWindow.R_RaceLive.item( row, column )
				if i == None:
					i = QTableWidgetItem( text )
					Globals.MainWindow.R_RaceLive.setItem(row, column, i )
				else:
					i.setText( text )
				i.setBackground( brush )
				if icon is not None:
					i.setIcon( icon )
				else:
					i.setIcon( QIcon() )
			except  Exception as e:
				print("in update, setLine( color,%d,%d,%s)"%(row, column, text))
				print( color )
				print( e )

		curtime = int( time())-self.start_time
		if self._status == self.cmdStart:
			Globals.MainWindow.PB_TimeRace.setFormat(
				"%s / %s - %%p%%"%( createTimeSeconds( curtime ), createTimeSeconds(self._duration) )
				)
		elif self._status == self.cmdEndTime:
			Globals.MainWindow.PB_TimeRace.setFormat(
				"Time finished: %s, Laps %d/%d  - %%p%%"%( createTimeSeconds( curtime ), self.remain_lap, self._laps )
				)
		elif self._status == self.cmdFinish:
			Globals.MainWindow.PB_TimeRace.setFormat(
				"Finish Flag: %s - %%p%%"%( createTimeSeconds( curtime ) )
				)

		Globals.MainWindow.PB_TimeRace.setProperty("value",  curtime )
		for task in receiver:
				r = receiver[task]
				q = r['queue']['race']
				while not q.empty():
					e = q.get_nowait()
					tp 		= e.tp
					millis 	= e.millis
					type		= e.type
					try:
						self.doRace( tp, millis, type)
					except  Exception as e:
						print("in manageRace.update")
						print( e )

		Globals.MainWindow.R_RaceLive.setRowCount( self.maxrows )
		l = self._duration*4000
		for tp in dictRace:
			tt = dictRace[tp]
			if tt["updated"]:
				row 	= tt["row"]
				setLine( colors["White"], row, 0, "%3.3d%-10.10x"%(tt["lapcount"],int(l - tt["remticks"])))
				setLine( colors["White"], row, 1, "%-3d, %s"%(tt["ridernum"], tt["ridername"]) )
				if tt["ended"]:
					setLine( colors["White"], row, 2, "%3.3d"%tt["lapcount"], icons["finish flag"])
				else:
					setLine( colors["White"], row, 2, "%3.3d"%tt["lapcount"],  None)
				setLine( colors["White"], row, 3, createTime(tt["remticks"]))
				if tt["lapcount"] > 0:
					setLine( tt["textcolor"], row, 4, createTime(tt["lastlap"]))
				if tt["lapcount"] > 1:
					setLine( tt["textcolor"], row, 5, createTime(tt["bestlap"]))
				tick 	= tt["lasttick"]
				dur		= self._duration * 1000
				for i in range( 0,  self.partials  ):
					val = tt["partial"][i] - tick
					if val <= 0 or val>dur or tt["partial"][i] < tt["lasttick"] :
						txt = ""
						val = 0
					else:
						txt =  createTime( val )
					setLine( colors["White"], row,  self._basecol  + i, txt )
					tick = tt["partial"][i]
		Globals.MainWindow.R_RaceLive.sortItems(0, Qt.DescendingOrder)

	def doRace( self, tp,  millis, type ):
		lap	= 0
		raceTime = int(time())

		try:
			if tp in dictRace:														# test if transponder it registred
				tt 	= dictRace[tp]
				ptt	= self.private[tp]
				if not tt["ended"]:													# has the rider passed the finish flag
					if type == 0:													# finish line crossing
						lap				= millis - tt["lasttick"]
						tt["lasttick"] 	= millis
						tt["lastlap"]		= lap
						tt["remticks"] 	= time()*1000 - self.start_time_ms
						tt["time"]		= raceTime
						if tt["lapcount"] > 0:										# the first crossing, it not a full lap
							if lap < tt["bestlap"]:
								tt["textcolor"]	= colors["Green"]
								tt["bestlap"] 		= lap
							else:
								tt["textcolor"]	= colors["White"]
						tt["lapcount"]		+=1										# add a lap
						tt["updated"]		= True									# all updated
						ptt[0]	= tt["lapcount"]
						ptt[1]	= -tt["remticks"]
						if self.max_time < raceTime:		# we have finished the time .....
							cl = sorted(self.private.items(), reverse=True,  key=lambda t:t[1])
							if cl[0][0] == tp:							# ok leader passed the line
								if self.remain_lap == -2:				# start for the last laps...
									self._status		= self.cmdEndTime
									self.remain_lap 	= self._laps
								else:
									self.remain_lap -= 1
									if self.remain_lap == 0:
										self._status = self.cmdFinish
										tt["ended"] = True
						if self._status == self.cmdFinish:
							tt["ended"] = True
					else:
						tt["partial"][type-1] 	= millis
						tt["updated"]			= True
			else:
				tt = {}
				if type == 0:
					tt["lapcount"] = 1 									# R_lapcount
				else:
					tt["lapcount"] = 0 									# R_lapcount
				tt["remticks"] = time()*1000 - self.start_time_ms				# R_remticks
				tt["bestlap"] 	= self._duration*1000 						# R_bestlap
				tt["lastlap"] 	= 0 										# R_lastlap
				tt["totticks"] = self._duration*1000 						# R_totticks
				if Globals.C_concurrents_TP_fmt%tp in Globals.tpRacerList :
					c	= Globals.racerList[ Globals.tpRacerList[ Globals.C_concurrents_TP_fmt%tp ] ]
					tt['ridername']			= "%s,%s"%(c['nom'],c['prenom'])		# I_ridername
					tt['ridernum']				= c['numero']						# I_ridernum
				else:
					tt["ridername"]	="Unknow TP_%d"%tp
					tt["ridernum"] 	= 0
				if type == 0:
					tt["lasttick"] 	= millis							# R_lasttick
				else:
					tt["lasttick"] 	= self.start_time*1000				# R_lasttick
				tt["updated"] 		= True 								# R_updated
				tt["textcolor"]	= colors["Cyan"]					 	# R_textcolor
				tt["ended"]		= False 								# R_ended
				tt["partial"]		= []
				for i in range( 0,  self.partials ):
					if i == ( type - 1 ):
						tt["partial"].append( millis )
					else:
						tt["partial"].append(0)
				tt["row"]			= self.maxrows
				dictRace[tp] = tt
				self.maxrows		+= 1
				ptt = []
				ptt.append( tt["lapcount"] )
				ptt.append( -tt["remticks"] )
				self.private[tp] = ptt


		except  ValueError:
			print("got an error")
