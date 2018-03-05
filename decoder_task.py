# 7846F300047B48
# set @p=0;
# select id,timecode,transponder,millis-@p as diff,@p:=millis as millis from passage where transponder = 70379;
from threading 		import Thread
import socket
import struct
#import sys
#import mysql.connector
import serial
#from mysql.connector        import Error

class decoder_task():
	task			= dict([])
	soc_ip		= "224.3.29.71"
	soc_port		= 10000

	def __init__(self, sdev, baud=115200):
		print( sdev )
		try:
			d = self.task[ sdev ]
			return
		except:

			d					= dict()
			d['device']		= sdev
			d['ip']			= self.soc_ip
			d['port']		= self.soc_port + len( self.task )
			d['baud']		= baud

			p = Thread( target=self.decoder, args=(d['device'], d['baud'], d['ip'], d['port']))
			d['pid']			= p
			self.task[sdev]	= d
			p.setDaemon( True )
			p.start()


	def decoder(self, device, baud,  ip, port):
		theSer = serial.Serial( device, baud)
		if not theSer.is_open:
			print( "ERROR Opening: ")
			print( device)
			print("\n")
			exit( -2)
#try :
# Connect to the database
#	 cnx = mysql.connector.connect(user='cano',host='127.0.0.1',database='cano')
#	 csr = cnx.cursor()
#except Error as e:
#	print(e)
#	exit(-3)
#finally:
#	print("DB Ok")
#cmd = "INSERT INTO passage (id,timecode,transponder,millis) VALUE (NULL,NOW(),%s,%s)"
		multicast_group = (ip,port)

# Create the datagram socket
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Set a timeout so the socket does not block indefinitely when trying
# to receive data.
		sock.settimeout(0.1)
# Set the time-to-live for messages to 1 so they do not go past the
# local network segment.
		ttl = struct.pack('b', 10)
		sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)
		theSer.write("VERSION\r\n")
		theSer.write("CANO MODE\r\n")

		while(1):
			line = theSer.readline()
			if len(line)==(16):
				tp		= int( line[0:5]	, 16 )
				millis	= int( line[6:]	, 16 )
#				data = (
#				    tp,
#				    millis
#				    )
#				try:
#					csr.execute( cmd,data )
#					cnx.commit()
#				except Error as e:
#					print(e)
#				finally:
#					print (line)
				try:
					message = str(tp) +" " + str( millis )
					sock.sendto(message, multicast_group)
				except socket.timeout:
					print("exception on send multicast")
				finally:
					message=""
			else:
				print( line )
				print( len( line ))
				print( "\n")
		#close the connection
#		cnx.close()
		exit(0)
