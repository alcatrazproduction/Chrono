#!/usr/bin/python
######################################################################################
# (c) Yves Huguenin, yves.huguenin@free.fr, mars 2018							#
# 15.03.2018:	Modified to have right partial crossing							#
######################################################################################
# Decoder interface class to be dinamicaly loaded								#
# main entry point is member function createThread( self, storage, pref,name )		#
# Input:																#
#	storage:		Dictionary with all the needed infos						#
#				multi_ip		multicast ip								#
#				port			the assigned port							#
#	pref:		The preferences Dict ( all the settings )					#
#	name:		the class name											#
#																	#
# Return the task pointer												#
# the class must be decoder, and not the filename !							#
#																	#
######################################################################################
# Simulator for develloping 												#
#	on the preference must provide:										#
#		howmany		= Number of transponder to simulate					#
#		laptime		= the minimum laptime to simulate						#
#		delay		= the minimum delay for partial to simulate, an entry with	#
#					  a value of zero (0) is mandatory, to simulate the finish	#
#					  line											#
#		auto_assign	= if True, the transponder will be assigned automatically	#
#					  only mandatory to the Type 0 ( finish line ), other are	#
#					  not probed										#
#																	#
######################################################################################

from threading 		import Thread
from time 			import time, sleep
import socket
import struct
from random 			import randrange
import Globals

# index in transponder list

i_finish			= 0
i_laps			= 1
i_partial			= 2
i_lastline		= 3

factor			= 1000						# Multiply factor for ticks

class decoder():
	tp_base		= 1000000						# Base number from the transponder, will be incremented
	transponder	= {}							# Dict to save the transponder params
	howmany		= 0							# number of transponder to create
	laptime		= 10000000000					# laptime, only set in type = 0
	sockets		= {}							# dict for sockets used list
	mgroup		= {}							# dist for multicast group
	partials		= {}							# dict for partial
	theThead		= None

	def createThread(self,d,  decoder, name):

		if self.howmany < decoder['howmany']:
			self.howmany = decoder['howmany']

		i 		= len( self.transponder )
		while len( self.transponder ) < self.howmany:
			self.transponder[self.tp_base+i]		= []
			self.transponder[self.tp_base+i].append(						# init time start
											int( time()*factor )
											)
			self.transponder[self.tp_base+i].append( 0 )						# lapnumber
			self.transponder[self.tp_base+i].append( {} )					# partial crossing time
			self.transponder[self.tp_base+i].append( 0 )						# lastline crossing
			i += 1
		type		= decoder['type']
		delay	= decoder['delay']*factor
		if  decoder['type'] == 0 and  decoder['auto_assign']:
			print( "Auto assign Transponder activated")
			i = 0
			rl = Globals.MainWindow.L_racerlist
			for c in range( 0,  rl.count()):
				t = rl.item(c).data(Globals.UserRole)
				Globals.racerList[t]['transponder'] = self.tp_base+i

				Globals.tpRacerList[ Globals.C_concurrents_TP_fmt%( self.tp_base+i ) ] = t
				i += 1
#				if i > self.howmany:
#					break
		try:														# init the socket
			self.mgroup[ type ] 	= (d['multi_ip'],d['port'])
			sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			sock.settimeout(0.1)
			ttl = struct.pack('b', 10)
			sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)
			self.sockets[ type ]	= sock
		except Exception as e:
			print("in simulator.createThread( socket creation ) got Error")
			print( e )

		if decoder['type'] == 0:										# only create Thread on type 0 ( finishline )
			self.laptime	= decoder['laptime'] * factor					# Set the minimum laptime
			self.theThead 	= Thread( target=self.decoder, args=(decoder['laptime'],
										decoder['delay'],
										d['multi_ip'],
										d['port'],
										decoder['type'])
										)
		else:													# otherwise simply add the delay in list
			for t in self.transponder:
				tp = self.transponder[t]
				tp[i_partial][type] = tp[i_finish]
			self.partials[decoder['type']] = delay
		return self.theThead



	def decoder(self,  laptime, delay,  ip, port,  type):

		while(1):																# loop forever
			tc = int(time()*1000)												# get timecode
			tp = randrange( self.tp_base, self.tp_base + len( self.transponder ))			# take a random transponder
			ll = self.transponder[ tp ]											# get transponder data
			ok = False														# ok the send datas
			sp = sorted( self.partials.items() )									# sorted list of partial
			if ll[i_lastline] == 0:												# last was finish
				if len( self.partials ) == 0:										# only finish line, no partial
					if ( ll[i_finish] + self.laptime ) <= tc:						# ok good to end
						ok = True
						ll[i_finish] 	= tc
				else:														# we have partials
					if ( ll[i_finish] + sp[0][1] ) <= tc:							# ok passed the first partial
						ok = True
						ll[i_partial][ sp[0][0] ] = tc
						ll[i_lastline] = sp[0][0]								# set the crossing to the first partial
			elif ll[i_lastline] == sp[ len(sp) - 1 ][0]:								# the last was the final partial
				if ( ll[i_finish] + self.laptime ) <= tc:							# ok good to end
					ok = True
					ll[i_finish] 	= tc
					ll[i_lastline] = 0											# set finish line passed
			else:															# we have more than one partial
				ap	= sp.index( (ll[i_lastline], self.partials[ll[i_lastline]]) )		# get the index of the last partial
				if ( ll[i_partial][sp[ap][0]] + sp[ap+1][1] ) <= tc:					# ok, time is good, we passed it
					ap						+= 1								# select next one
					ll[i_lastline]				= sp[ap][0]						# set the last passed line
					ll[i_partial][sp[ap][0]]		= tc								# update crossing
					ok = True
# ####################
			if ok:
				try:
					message = str(tp) +" " + str( tc )
					self.sockets[ll[i_lastline]].sendto(message.encode(), self.mgroup[ll[i_lastline]])
				except socket.timeout:
					print("exception on send multicast")
				finally:
					message=""

			sleep( randrange(50, 1000) / factor)
		exit(0)
