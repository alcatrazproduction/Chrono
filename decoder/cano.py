#!/usr/bin/python
######################################################################################
# (c) Yves Huguenin, yves.huguenin@free.fr, mars 2018							#
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
# interface to the cano decoder, standard mode								#
#	on the preference must provide:										#
#		device	= serial device name ( Unix = /dev/tty....; Win = COMx )		#
#		baud		= baud rate ( default: 115200 )							#
#																	#
######################################################################################

from threading 		import Thread
import socket
import struct

import serial


class decoder():
	task			= dict([])

	def createThread(self,d,  decoder, name):
			p = Thread( target=self.decoder, args=(decoder['device'], decoder['baud'],  d['multi_ip'], d['port']))
			return p

	def decoder(self, device, baud,  ip, port):
		theSer = serial.Serial( device, baud)
		if not theSer.is_open:
			print( "ERROR Opening: ")
			print( device)
			print("\n")
			exit( -2)

		multicast_group = (ip,port)

		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sock.settimeout(0.1)

		ttl = struct.pack('b', 10)
		sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)
		theSer.write('VERSION\r\n'.encode())
		theSer.write('CANO MODE\r\n'.encode())

		while(1):
			line = theSer.readline()
			if len(line)==(16):
				tp		= int( line[0:5]	, 16 )
				millis	= int( line[6:]	, 16 )
				try:
					message = str(tp) +" " + str( millis )
					sock.sendto(message.encode(), multicast_group)
				except socket.timeout:
					print("exception on send multicast")
				finally:
					message=""
			else:
				print( line )
				print( len( line ))
				print( "\n")
		exit(0)
