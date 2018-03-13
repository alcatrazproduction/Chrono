#!/usr/bin/python3 .
######################################################################################
# (c) Yves Huguenin, yves.huguenin@free.fr, mars 2018							#
######################################################################################
from time 			import time
from PyQt5.QtCore		import QTimer, Qt
from PyQt5.QtGui		import QBrush
from PyQt5.QtWidgets 	import QTableWidgetItem
from Globals			import receiver, colors, decoder, createTimeSeconds
from Globals			import dictRace, createTime
from queue			import Queue
import Globals

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
		self._status		= self.cmdWaiting
		self.start_time	= int( time() )
		self.max_time		= self.start_time + self._duration
		self.remain_lap	= -2
		Globals.MainWindow.B_Stop.setEnabled(True)
		Globals.MainWindow.B_Start.setEnabled(False)
		Globals.MainWindow.R_RaceLive.setColumnCount( self._basecol )
		Globals.MainWindow.R_RaceLive.setColumnHidden(0, True)

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
		self.partials		= col -  self._basecol
		Globals.MainWindow.PB_TimeRace.setMaximum( self._duration )
		Globals.MainWindow.PB_TimeRace.setProperty("value", 0)
		self.timer 		= QTimer()
		self.timer.timeout.connect(self.update)
		self.timer.start(1000)


	def update(self):
		def setLine( color, row, column, text):
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
			except  Exception as e:
				print("in update, setLine( color,%d,%d,%s)"%(row, column, text))
				print( color )
				print( e )

		curtime = int( time())-self.start_time
		Globals.MainWindow.PB_TimeRace.setFormat(
			"%s / %s - %%p%%"%( createTimeSeconds( curtime ), createTimeSeconds(self._duration) )
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
				setLine( colors["White"], row, 1, tt["ridername"])
				setLine( colors["White"], row, 2, "%3.3d"%tt["lapcount"])
				setLine( colors["White"], row, 3, createTime(tt["remticks"]))
				setLine( colors["White"], row, 4, createTime(tt["lastlap"]))
				setLine( colors["White"], row, 5, createTime(tt["bestlap"]))
				tick 	= tt["lasttick"]
				for i in range( 0,  self.partials-1  ):
					val = tt["partial"][i] - tick
					if val < 0 :
						val = 0
					setLine( colors["White"], row,  self._basecol  + i, createTime( val ) )
					tick = tt["partial"][i]
		Globals.MainWindow.R_RaceLive.sortItems(0, Qt.DescendingOrder)


	def doRace( self, tp,  millis, type ):
		lap	= 0
		raceTime = int(time())

		try:
			if tp in dictRace:
				tt = dictRace[tp]
				if not tt["ended"]:
					if type == 0:
						lap				= millis - tt["lasttick"]
						tt["lasttick"] 	= millis
						tt["lastlap"]		= lap
						tt["remticks"] 	= time()*1000 - self.start_time * 1000
						tt["time"]		= raceTime
						if lap < tt["bestlap"]:
							tt["bestlap"] 	= lap
						tt["lapcount"]		+=1
						tt["updated"]		= True
						if self.max_time < raceTime:		# we have finished the time .....
							cl = sorted(dictRace.items(), reverse=True,  key=lambda t:t[1])
							if cl[0][0] == tp:							# ok leader passed the line
								if self.remain_lap == -2:			# start for the last laps...
									self.remain_lap = self._laps
								else:
									self.remain_lap -= 1
									if self.remain_lap == 0:
										self._status = self.cmdFinish
										tt["ended"] = True
					else:
						tt["partial"][type-1] 	= millis
						tt["updated"]			= True
				if self._status == self.cmdFinish and type == 0:
					tt["ended"] = True

			else:
				if type == 0:
					tt = {}
					tt["lapcount"] = 1 										# R_lapcount
					tt["remticks"] = time()*1000 - self.start_time * 1000			# R_remticks
					tt["bestlap"] =self._duration*1000 						# R_bestlap
					tt["lastlap"] = 0 										# R_lastlap
					tt["totticks"] = self._duration*1000 						# R_totticks
#					if tp in rider_name :
#						tt["ridername"] =rider_name[tp][0]						# R_ridername
#						tt["ridernum"] =rider_name[tp][1]						# R_ridernum
#					else:
					tt["ridername"]	="Unknow TP_%d"%tp
					tt["ridernum"] 	= 0
					tt["lasttick"] 	= millis								# R_lasttick
					tt["updated"] 		= True 								# R_updated
					tt["textcolor"]	= Globals.text_inverted + Globals.text_blue 	# R_textcolor
					tt["ended"]		= False 								# R_ended
					tt["partial"]		= []
					for i in range( 0,  self.partials ):
						tt["partial"].append(0)
					tt["row"]			= self.maxrows
					dictRace[tp] = tt
					self.maxrows		+= 1

		except  ValueError:
			print("got an error")
