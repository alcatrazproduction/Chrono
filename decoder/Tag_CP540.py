#!/usr/bin/python
######################################################################################
# (c) Yves Huguenin, yves.huguenin@free.fr, mars 2018								 #
######################################################################################
# Decoder interface class to be dinamicaly loaded									 #
# main entry point is member function createThread( self, storage, pref,name )		 #
# Input:																			 #
#	storage:		Dictionary with all the needed infos							 #
#				multi_ip		multicast ip										 #
#				port			the assigned port									 #
#	pref:		The preferences Dict ( all the settings )							 #
#	name:		the class name														 #
#																					 #
# Return the task pointer															 #
# the class must be decoder, and not the filename !									 #
#																					 #
######################################################################################
# Tag Heuer CP520 																	 #
#	on the preference must provide:													 #
#		device	= serial device name ( Unix = /dev/tty....; Win = COMx )			 #
#		baud		= baud rate ( default: 2400,9600,38400,57600 )					 #
#																					 #
######################################################################################

from threading 		import Thread
#from crccheck.crc 		import Crcc16Mcrf4xx as crc16 			# use crc16.calc( bytearray( [data].encode() ) )
import socket
import struct
import serial

# Command Definition
TAB				= chr( 0x09 )						# Tabulate character
CRLF			= chr( 0x0D ) + chr( 0x0A )			# EndLine ( /r/n )
cmd_CP2PC		= {}

test_passing	= "<STA 006141 00:02'57\"541 38 07 0 1569>"
class passing():
	def __init__(self, data = ""):
		self.telegram		= data
		try:
			if data[0:1] == '<':
				self.loop_ID		= data[1:4]
				self.tp			= int( data[5:11]  )
				self.hours		= int( data[12:14] )
				self.minutes		= int( data[15:17] )
				self.seconds		= int( data[18:20] )
				self.millis		= int( data[21:24] )
				self.power		= int( data[25:27] )
				self.loopcout		= int( data[28:30] )
				self.btpower		= int( data[31:32] )
				self.checksum		= int( data[33:37] )
				byte				= bytearray( data[1:33].encode() )
				compute			= 0
				for i in range(0,32):
					compute		+= byte[i]
				if compute == self.checksum:
					self.valid	= True
				else:
					self.valid	= False
			else:
				self.valid		= False
		except Exception as e:
			print( e )
			self.valid			= False




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

# Command Definition
	def getStatus( self ): 																		#TODO:
		self.sendCmd( self.cmd['Status'] )
#		response:	[STATUS]
	def start( self ): 																		#TODO:
		self.sendCmd( self.cmd['Start'] )
#		response:	[DEPART] or none if decoder already started
	def setConfig( self ,  cfg ): 																		#TODO:
#		Update decoder configuration
#		command:	ESC + 0x08 + 0x08 + [CONFIG] + [CRC] + '>'
#		response:	none
		crc = crc16( bytearray( cfg.encode() ) )
		self.sendCmd( self.cmd['Set Config']%(cfg, crc) )
	def setIPConfig( self,  cfg ): 																		#TODO:
#		Update decoder IP configuration. Note: Decoder must be stopped
#		before issuing this command (why?)
#		command:	ESC + 0x09 + 0x09 + [IPCONFIG] + [CRC] + '>'
		crc = crc16( bytearray( cfg.encode() ) )
		self.sendCmd( self.cmd['Set IP Config']%(cfg, crc) )
#		response:	XPORT specific (TBC)
	def getConfig( self ): 																		#TODO:
#		Fetch current decoder configuration & identification
#		command:	ESC + 0x10
		self.sendCmd( self.cmd['Get Config'] )
#		response:	[DECODERCONF]
#
	def acknowledge( self, status ): 																		#TODO:
		if status:
			self.sendCmd( "AK C" )
		else:
			self.sendCmd( "AK F" )
#		response:	none or [PASSING]
#
	def repeat( self ): 																		#TODO:
#		Repeat first unacknowledged passing, else last acknowledged passing
#		command:	ESC + 0x12
		self.sendCmd( self.cmd['Repeat'] )
#		response:	[PASSING]
#
	def stop( self ): 																		#TODO:
#		Stop decoder
#		command:	ESC + 0x13 + '\'
		self.sendCmd( self.cmd['Stop'] )
#		response:	[STOP] (even if already stopped)
#
	def setTime( self ,  cfg ): 																		#TODO:
#		Update decoder time of day - also sets running time if decoder
#		started and config option "Running time to time of decoder" set
#		command:	ESC + 0x48 + [SETTIME] + 't'
		self.sendCmd( self.cmd['Start']%( cfg ) )
#		response:	none
#
	def setDate( self,  cfg ): 																		#TODO:
#		Update decoder date
#		command:	ESC + 0x0a + 0x0a + [SETDATE] + [CRC] + '>'
		crc = crc16( bytearray( cfg.encode() ) )
		self.sendCmd( self.cmd['Set Date']%( cfg, crc ) )
#		response:	none
#
	def setSTALevel( self,  cfg ): 																		#TODO:
#		Set detection level on STA channel
#		command:	ESC + 0x1e + [SETLEVEL]
		self.sendCmd( self.cmd['Set STA Level']%(cfg) )
#		response:	none
#
	def setBOXLevel( self,  cfg ): 																		#TODO:
#		Set Detection level on BOX channel
#		command:	ESC + 0x1f + [SETLEVEL]
		self.sendCmd( self.cmd['Set BOX Level']% ( cfg ) )
#		response:	none
#
	def statBXX( self,  cfg ): 																		#TODO:
#		Request status on remote decoder with id specified in B
#		command:	ESC + 0x49 + [B]
		self.sendCmd( self.cmd['Stat BXX']%( cfg ))
#		response:	(TBC)
#
	def bXXLevel( self ): 																		#TODO:
#		Increment all detection levels by 0x10 (Note 2)
#		command:	ESC + 0x4e + 0x2b
		self.sendCmd( self.cmd['BXX  Level'] )
#		response:	none

	def	sendCmd( self,  command): 																		#TODO:
		print( command )

	def	receiveResponse( self,  timeout = 0 ): 																		#TODO:
		print( timeout )
		return ''
