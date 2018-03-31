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

# Command Definition (Send CP540 to PC )
	def sendAcknowledge( self, status ):
		if status:
			self.sendCmd( "AK C" )
		else:
			self.sendCmd( "AK F" )

	def sendIdent( self, ident ):
		self.sendCmd( "ID %5.5d"%ident )

	def sendOpenRun( self, run, added,  timming ):
		self.sendCmd( "OP %2.2d T%2.2d %19.19s"%(run, added, timming) )

	def sendCloseRun( self, run ):
		self.sendCmd( "CL %2.2d"%(run) )

	def sendRunStart( self, run, added,  timming ):
		self.sendCmd( "DS %2.2d T%2.2d %19.19s"%(run, added, timming) )

	def sendRunEnd( self, run ):
		self.sendCmd( "DE %2.2d"%(run) )

	def sendNewTime( self, cid, seq, channel,  hrs, mins, secs, fracs, days  ):
		if channel not in ('M1', 'M2', 'M3', 'M4'):
			try:
				channel = "%2.2d"%channel
			except:
				channel = 'M1'
		self.sendCmd( "TN %4.4d %4.4d %2.2s %2.2d:%2.2d:%2.2d.%5.5d %5.5d"%
			(cid, seq, channel, hrs, mins, secs, fracs, days) )

	def sendUnassingedTime( self, cid, seq, channel,  hrs, mins, secs, fracs, days  ):
		if channel not in ('M1', 'M2', 'M3', 'M4'):
			try:
				channel = "%2.2d"%channel
			except:
				channel = 'M1'
		self.sendCmd( "T- %4.4d %4.4d %2.2s %2.2d:%2.2d:%2.2d.%5.5d %5.5d"%
			(cid, seq, channel, hrs, mins, secs, fracs, days) )

	def sendReindentTime( self, cid, seq, channel,  hrs, mins, secs, fracs, days  ):
		if channel not in ('M1', 'M2', 'M3', 'M4'):
			try:
				channel = "%2.2d"%channel
			except:
				channel = 'M1'
		self.sendCmd( "T* %4.4d %4.4d %2.2s %2.2d:%2.2d:%2.2d.%5.5d %5.5d"%
			(cid, seq, channel, hrs, mins, secs, fracs, days) )

	def sendManualTime( self, cid, seq, channel,  hrs, mins, secs, fracs, days  ):
		if channel not in ('M1', 'M2', 'M3', 'M4'):
			try:
				channel = "%2.2d"%channel
			except:
				channel = 'M1'
		self.sendCmd( "T+ %4.4d %4.4d %2.2s %2.2d:%2.2d:%2.2d.%5.5d %5.5d"%
			(cid, seq, channel, hrs, mins, secs, fracs, days) )

	def sendDuplicateTime( self, cid, seq, channel,  hrs, mins, secs, fracs, days  ):
		if channel not in ('M1', 'M2', 'M3', 'M4'):
			try:
				channel = "%2.2d"%channel
			except:
				channel = 'M1'
		self.sendCmd( "T= %4.4d %4.4d %2.2s %2.2d:%2.2d:%2.2d.%5.5d %5.5d"%
			(cid, seq, channel, hrs, mins, secs, fracs, days) )

	def sendCancelTime( self, cid, seq, channel,  hrs, mins, secs, fracs, days  ):
		if channel not in ('M1', 'M2', 'M3', 'M4'):
			try:
				channel = "%2.2d"%channel
			except:
				channel = 'M1'
		self.sendCmd( "TC %4.4d %4.4d %2.2s %2.2d:%2.2d:%2.2d.%5.5d %5.5d"%
			(cid, seq, channel, hrs, mins, secs, fracs, days) )

	def sendItermediateResult( self, iid,  cid, hrs, mins, secs, fracs  ):
		self.sendCmd( "IR %1.1d    %4.4d    %2.2d:%2.2d:%2.2d.%5.5d"%
			(iid, cid, hrs, mins, secs, fracs) )

	def sendDifferentialResult( self, winner,  looser, hrs, mins, secs, fracs  ):
		self.sendCmd( "DR %4.4d %4.4d    %2.2d:%2.2d:%2.2d.%5.5d"%
			(winner, looser, hrs, mins, secs, fracs) )

	def sendRunResult( self, ranq,  cid, hrs, mins, secs, fracs  ):
		self.sendCmd( "RR %4.4d %4.4d    %2.2d:%2.2d:%2.2d.%5.5d"%
			(ranq, cid, hrs, mins, secs, fracs) )

	def sendAddResult( self, ranq,  cid, hrs, mins, secs, fracs  ):
		self.sendCmd( "GR %4.4d %4.4d    %2.2d:%2.2d:%2.2d.%5.5d"%
			(ranq, cid, hrs, mins, secs, fracs) )

	def sendSpeed( self, snum,  cid, speed, unit ):
		self.sendCmd( "VE %1.1d %4.4d %3.3f %7.7s"%
			(snum, cid, speed, unit ) )

	def sendRecallOriginal( self, cid, seq, channel,  hrs, mins, secs, fracs, days  ):
		if channel not in ('M1', 'M2', 'M3', 'M4'):
			try:
				channel = "%2.2d"%channel
			except:
				channel = 'M1'
		self.sendCmd( "AN %4.4d %4.4d %2.2s %2.2d:%2.2d:%2.2d.%5.5d %5.5d"%
			(cid, seq, channel, hrs, mins, secs, fracs, days) )

	def sendRecallDeidentified( self, cid, seq, channel,  hrs, mins, secs, fracs, days  ):
		if channel not in ('M1', 'M2', 'M3', 'M4'):
			try:
				channel = "%2.2d"%channel
			except:
				channel = 'M1'
		self.sendCmd( "A- %4.4d %4.4d %2.2s %2.2d:%2.2d:%2.2d.%5.5d %5.5d"%
			(cid, seq, channel, hrs, mins, secs, fracs, days) )

	def sendRecallReindentified( self, cid, seq, channel,  hrs, mins, secs, fracs, days  ):
		if channel not in ('M1', 'M2', 'M3', 'M4'):
			try:
				channel = "%2.2d"%channel
			except:
				channel = 'M1'
		self.sendCmd( "A* %4.4d %4.4d %2.2s %2.2d:%2.2d:%2.2d.%5.5d %5.5d"%
			(cid, seq, channel, hrs, mins, secs, fracs, days) )

	def sendRecallManual( self, cid, seq, channel,  hrs, mins, secs, fracs, days  ):
		if channel not in ('M1', 'M2', 'M3', 'M4'):
			try:
				channel = "%2.2d"%channel
			except:
				channel = 'M1'
		self.sendCmd( "A+ %4.4d %4.4d %2.2s %2.2d:%2.2d:%2.2d.%5.5d %5.5d"%
			(cid, seq, channel, hrs, mins, secs, fracs, days) )

	def sendRecallDuplicate( self, cid, seq, channel,  hrs, mins, secs, fracs, days  ):
		if channel not in ('M1', 'M2', 'M3', 'M4'):
			try:
				channel = "%2.2d"%channel
			except:
				channel = 'M1'
		self.sendCmd( "A= %4.4d %4.4d %2.2s %2.2d:%2.2d:%2.2d.%5.5d %5.5d"%
			(cid, seq, channel, hrs, mins, secs, fracs, days) )

	def sendRecallCancel( self, cid, seq, channel,  hrs, mins, secs, fracs, days  ):
		if channel not in ('M1', 'M2', 'M3', 'M4'):
			try:
				channel = "%2.2d"%channel
			except:
				channel = 'M1'
		self.sendCmd( "AC %4.4d %4.4d %2.2s %2.2d:%2.2d:%2.2d.%5.5d %5.5d"%
			(cid, seq, channel, hrs, mins, secs, fracs, days) )

	def sendRequestID( self ):
		self.sendCmd( "#ID" )
			
	def sendPrintLine( self, text  ):
		self.sendCmd( "#PL %24.24s"%
			(text) )

	def sendDownload( self, run):
		self.sendCmd( "#DL %2.2d"%
			(run) )

	def sendRecallTime( self, seq,  channel):
		self.sendCmd( "#RT %4.4d %2.2d"%
			(seq, channel) )

	def sendDeleteStartList( self):
		self.sendCmd( "#SLR" )

	def sendAdd2StartList( self, cid):
		self.sendCmd( "#SLA %4.4d"%
			( cid ) )

	def sendCloseStartList( self ):
		self.sendCmd( "#SLC" )


	def	sendCmd( self,  command):
		sum	= 0
		for i in bytearray( command.encode()):
			sum += i
		sum = sum % 65536
		print( "%s%s%d%s"%(command, TAB, sum, CRLF ) )

	def	receiveResponse( self,  timeout = 0 ): 																		#TODO:
		print( timeout )
		return ''
