#!/usr/bin/python
######################################################################################
# (c) Yves Huguenin, yves.huguenin@free.fr, mars 2018							#
######################################################################################
from Globals	import dictBestLap
from Globals 	import dictRace
from Globals	import createTime
import Globals
#import socket
#import struct
#import thread
import time

# ***********************************************************************************************************************
# * displayClassementBestLap(  )
# * Display the best lap time
# *
# * Created:   28.01.2018	Yves Huguenin
# *
# ***********************************************************************************************************************
def displayClassementBestLap():

	classement = sorted(dictBestLap.items(), key=lambda t:t[1])
	print ('============================================================================================')
	print ('|{:20s}'.format( "Rider Name") +
		' | {:8s}'.format( "Dossard") +
		" | "+ "   Best Lap   " +
		" | "+ "   Lap Time   " +
		' | {:15s}'.format("Transponder"  ) +
		' | {:3s}'.format("Lap")+
		' |')
	print ('|=====================|==========|================|================|=================|=====|')
	for rider in classement:
		try:
			color 						= rider[1]["textcolor"]
			rider[1]["textcolor"]	= Globals.text_normal + Globals.text_black
			print ( color +'|{:20s}'.format( rider[1]["ridername"]) +
				' | {:8d}'.format( rider[1]["ridernum"]) +
				" | "+createTime( rider[1]["bestlap"]) +
				" | "+ createTime( rider[1]["lastlap"] ) +
				' | {:15d}'.format(rider[0]) +
				' | {:3d}'.format(rider[1]["lapcount"])+
				' |')
		except ( ValueError,  IndexError ) as e:
			print ( e )
			print (rider)
	print (Globals.text_normal +Globals.text_black+
		'|=====================|==========|================|================|=================|=====|')

# ***********************************************************************************************************************
# * displayClassementBestLap(  )
# * Display the best lap time
# *
# * Created:   28.01.2018	Yves Huguenin
# *
# ***********************************************************************************************************************
def displayClassementRace():

	classement = sorted(dictRace.items(), reverse=True,  key=lambda t:t[1])
	print ('===============================================================================================================')
	print ('|{:20s}'.format( "Rider Name") +
		' | {:8s}'.format( "Dossard") +
		" | "+ "   Best Lap   " +
		" | "+ "   Lap Time   " +
		' | {:15s}'.format("Transp. Race"  ) +
		' | {:3s}'.format("Lap")+
		' |'+
		' | '+ '   Race Time  '+
		' |')
	print ('|=====================|==========|================|================|=================|=====|=|================|')
	pos = 0;
	for rider in classement:
		try:
			pos += 1
			rr = rider[1]
			if rr["updated"]:
				if pos > rr["lastpos"]:
					color 					= Globals.text_inverted + Globals.text_red
				else:
					if pos < rr["lastpos"]:
						color 				= Globals.text_inverted + Globals.text_green
					else:
						color 				= Globals.text_inverted + Globals.text_blue
			else:
				color 						= Globals.text_normal + Globals.text_black
			rr["updated"] 	= False
			rr["lastpos"]	= pos
			if rr["ended"]:
				flag="*"
			else:
				flag=" "
			print ( color +'|{:20s}'.format( rr["ridername"]) +
				' | {:8d}'.format( rr["ridernum"]) +
				" | "+createTime( rr["bestlap"]) +
				" | "+ createTime( rr["lastlap"] ) +
				' | {:15d}'.format(rider[0]) +
				' | {:3d}'.format(rr["lapcount"])+
				' |{:1s}'.format( flag )+
				'| '+ createTime(int( ( rr["time"] - race_info['start_time'] )*4000 ) )+
				' |')
		except ( ValueError,  IndexError ) as e:
			print ( e )
			print (rider)
	print (Globals.text_normal +Globals.text_black+
		'|=====================|==========|================|================|=================|=====|=|================|')
	theTime = int( race_info['end_time']  * 4000 ) - int( time.time()  * 4000 )
	if theTime < 0:
		if race_info['lap'] == 0:
			print('Race ended')
		else:
			if race_info['lap'] == -2:
				print ( 'Time ended waiting for laps' )
			else:
				print('Time ended, Laps to go: {:2d}'.format( race_info['lap']))
	else:
		print ( 'Time remaining: {:10s}'.format( createTime( theTime )))

# ***********************************************************************************************************************
# * displayResultTask(  )
# * Main task to display the results
# *
# * Created:   28.01.2018	Yves Huguenin
# *
# ***********************************************************************************************************************
def displayResultTask():
	while True:
		print( Globals.clear_screen )
		print("in display task")
		if race_flag:
			print("Display Race classement")
			displayClassementRace()
		displayClassementBestLap()
		time.sleep( refresh_rate)

# ***********************************************************************************************************************
# * doBestLap( transponder number, ticks in 1/4 of milli-seconds )
# * Build the liste of the best lap time
# *
# * Created:   28.01.2018	Yves Huguenin
# *
# ***********************************************************************************************************************
def doBestLap( tp,  millis ):


	try:
		if tp in dictBestLap:
			tt = dictBestLap[tp]
			lap		= millis - tt["lasttick"]
			tt["lasttick"] = millis
			tt["lastlap"]	= lap
			if lap < tt["bestlap"]:
				tt["bestlap"] = lap
				tt["textcolor"] = Globals.text_inverted + Globals.text_green
			if lap > tt["bestlap"]:
				tt["textcolor"] = Globals.text_inverted + Globals.text_red
			tt["lapcount"]+=1
			tt["updated"]	= True
		else:
				dictBestLap.setdefault(tp, [])
				tt = dictBestLap[tp]
				tt["bestlap"]= max_time 					# I_bestlap
				tt["lastlap"] = 0 								# I_lastlap
				if tp in rider_name :
					tt["ridername"]=rider_name[tp][0]		# I_ridername
					tt["ridernum"]=rider_name[tp][1]		# I_ridernum
				else:
					tt.append("Unknow")
					tt.append(0)
				tt.append(millis)							# I_lasttick
				tt.append( 0 )								# I_lapcount
				tt.append( 0.999999999 )				# I_totticks
				tt.append( True )							# I_updated
				tt.append( Globals.text_inverted + Globals.text_blue )	# I_textcolor

	except  ValueError:
		print("got an error")

# ***********************************************************************************************************************
# * doRace( transponder number, ticks in 1/4 of milli-seconds )
# * Build the liste of the best lap time
# *
# * Created:   28.01.2018	Yves Huguenin
# *
#R_lapcount			= 0
#R_remticks			= 1
#R_bestlap			= 2
#R_lastlap			= 3
#R_time				= 4
#R_ridername			= 5
#R_ridernum			= 6
#R_lasttick			= 7
#R_updated			= 8
#R_lastpos			= 9
#R_ended				=10

# ***********************************************************************************************************************
def doRace( tp,  millis ):
	lap	= 0
	raceTime = time.time()

	try:
		if	not race_info['run']:
			return
		if tp in dictRace:
			tt = dictRace[tp]
			if not tt["ended"]:
				lap				= millis - tt["lasttick"]
				tt["lasttick"] 	= millis
				tt["lastlap"]		= lap
				tt["remticks"] 	= max_time - millis
				tt["time"]	= raceTime
				if lap < tt["bestlap"]:
					tt["bestlap"] = lap
				tt["lapcount"]+=1
				tt["updated"]	= True
				if race_info['end_time'] < raceTime:		# we have finished the time .....
					cl = sorted(dictRace.items(), reverse=True,  key=lambda t:t[1])
					if cl[0][0] == tp:							# ok leader passed the line
						if race_info['lap'] == -2:			# start for the last laps...
							race_info['lap'] = race_lap_full
						else:
							race_info['lap'] -= 1
							if race_info['lap'] == 0:
								race_info['ended'] = True
								tt[R_ended] = True
			if race_info['ended']:
				tt["ended"] = True

		else:
				dictRace.setdefault(tp, [])
				tt = dictRace[tp]
				tt["lapcount"] = 0 								# R_lapcount
				tt["remticks"] = max_time - millis 					# R_remticks
				tt["bestlap"] =max_time 					# R_bestlap
				tt["lastlap"] = 0 								# R_lastlap
				tt["totticks"] = raceTime 					# R_totticks
				if tp in rider_name :
					tt["ridername"] =rider_name[tp][0]		# R_ridername
					tt["ridernum"] =rider_name[tp][1]		# R_ridernum
				else:
					tt["lasttick"]="Unknow"
					tt["ridernum"] = 0
				tt["lasttick"] = millis							# R_lasttick
				tt["updated"] = True 							# R_updated
				tt["textcolor"]= Globals.text_inverted + Globals.text_blue 	# R_textcolor
				tt["ended"]= False 							# R_ended

	except  ValueError:
		print("got an error")


