#!/usr/bin/python
######################################################################################
# (c) Yves Huguenin, yves.huguenin@free.fr, mars 2018							#
######################################################################################

#from threading 		import Thread
import socket
import struct
import importlib
import serial
import Globals


class decoder_task():
	soc_ip		= "224.3.29.71"

	def __init__(self, decoder, name):
		print( decoder )
		try:
			d = Globals.decoder[ name ]
			return
		except:

			d					= dict()
			m					= importlib.import_module( decoder['class'] )
			d['class']			= m.decoder()
			d['multi_ip']			= self.soc_ip
			d['port']				= decoder['port']
			d['preferences']		= decoder

			p = d['class'].createThread( d,  decoder, name )
			d['pid']				= p
			Globals.decoder[name]	= d
			if p is not None:
				p.setDaemon( True )
				p.start()


	def x_decoder(self, device, baud,  ip, port):
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
