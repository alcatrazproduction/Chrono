#!/usr/bin/python
######################################################################################
# (c) Yves Huguenin, yves.huguenin@free.fr, mars 2018							#
######################################################################################
import socket
import struct
import thread
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
			color 						= rider[1][I_textcolor]
			rider[1][I_textcolor]	= text_normal + text_black
			print ( color +'|{:20s}'.format( rider[1][I_ridername]) +
				' | {:8d}'.format( rider[1][I_ridernum]) +
				" | "+createTime( rider[1][I_bestlap]) +
				" | "+ createTime( rider[1][I_lastlap] ) +
				' | {:15d}'.format(rider[0]) +
				' | {:3d}'.format(rider[1][I_lapcount])+
				' |')
		except ( ValueError,  IndexError ) as e:
			print ( e )
			print (rider)
	print (text_normal +text_black+
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
			if rr[R_updated]:
				if pos > rr[R_lastpos]:
					color 					= text_inverted + text_red
				else:
					if pos < rr[R_lastpos]:
						color 				= text_inverted + text_green
					else:
						color 				= text_inverted + text_blue
			else:
				color 						= text_normal + text_black
			rr[R_updated] 	= False
			rr[R_lastpos]	= pos
			if rr[R_ended]:
				flag="*"
			else:
				flag=" "
			print ( color +'|{:20s}'.format( rr[R_ridername]) +
				' | {:8d}'.format( rr[R_ridernum]) +
				" | "+createTime( rr[R_bestlap]) +
				" | "+ createTime( rr[R_lastlap] ) +
				' | {:15d}'.format(rider[0]) +
				' | {:3d}'.format(rr[R_lapcount])+
				' |{:1s}'.format( flag )+
				'| '+ createTime(int( ( rr[R_time] - race_info['start_time'] )*4000 ) )+
				' |')
		except ( ValueError,  IndexError ) as e:
			print ( e )
			print (rider)
	print (text_normal +text_black+
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
		print( clear_screen )
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
			lap		= millis - tt[I_lasttick]
			tt[I_lasttick ] = millis
			tt[I_lastlap]	= lap
			if lap < tt[I_bestlap]:
				tt[I_bestlap] = lap
				tt[I_textcolor] = text_inverted + text_green
			if lap > tt[I_bestlap]:
				tt[I_textcolor] = text_inverted + text_red
			tt[I_lapcount]+=1
			tt[I_updated]	= True
		else:
				dictBestLap.setdefault(tp, [])
				tt = dictBestLap[tp]
				tt.append( max_time )					# I_bestlap
				tt.append( 0 )								# I_lastlap
				if tp in rider_name :
					tt.append(rider_name[tp][0])		# I_ridername
					tt.append(rider_name[tp][1])		# I_ridernum
				else:
					tt.append("Unknow")
					tt.append(0)
				tt.append(millis)							# I_lasttick
				tt.append( 0 )								# I_lapcount
				tt.append( 0.999999999 )				# I_totticks
				tt.append( True )							# I_updated
				tt.append( text_inverted + text_blue )	# I_textcolor

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
#R_lastlap				= 3
#R_time			= 4
#R_ridername		= 5
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
			if not tt[R_ended]:
				lap				= millis - tt[R_lasttick]
				tt[R_lasttick ] 	= millis
				tt[R_lastlap]		= lap
				tt[R_remticks] 	= max_time - millis
				tt[R_time]	= raceTime
				if lap < tt[R_bestlap]:
					tt[R_bestlap] = lap
				tt[R_lapcount]+=1
				tt[R_updated]	= True
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
				tt[R_ended] = True

		else:
				dictRace.setdefault(tp, [])
				tt = dictRace[tp]
				tt.append( 0 )								# R_lapcount
				tt.append( max_time - millis )					# R_remticks
				tt.append( max_time )					# R_bestlap
				tt.append( 0 )								# R_lastlap
				tt.append( raceTime )					# R_totticks
				if tp in rider_name :
					tt.append(rider_name[tp][0])		# R_ridername
					tt.append(rider_name[tp][1])		# R_ridernum
				else:
					tt.append("Unknow")
					tt.append(0)
				tt.append(millis)							# R_lasttick
				tt.append( True )							# R_updated
				tt.append( text_inverted + text_blue )	# R_textcolor
				tt.append( False )							# R_ended

	except  ValueError:
		print("got an error")


