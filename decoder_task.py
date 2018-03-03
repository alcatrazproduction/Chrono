# 7846F300047B48
# set @p=0;
# select id,timecode,transponder,millis-@p as diff,@p:=millis as millis from passage where transponder = 70379;
from multiprocessing 		import Process
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
		try:
			d = self.task[ sdev ]
			return
		except:
			d	= dict([])
			d['device']		= sdev
			d['ip']			= self.soc_ip
			d['port']		= self.soc_port + self.task.count()
			d['baud']		= baud

			p = Process(target=decoder, args=(d))
			d['pid']			= p
			self.task[sdev]	= d

	def decoder(tk):
		theSer = serial.Serial( tk['device'], tk['baud'])
		if not theSer.is_open:
			print( "ERROR Opening: ")
			print( tk['device'])
			print("\n")
			exit( -2)
		tk['iop']				= theSer

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

		multicast_group = (tk['ip'], tk['port'])

# Create the datagram socket
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Set a timeout so the socket does not block indefinitely when trying
# to receive data.
		sock.settimeout(0.2)
# Set the time-to-live for messages to 1 so they do not go past the
# local network segment.
		ttl = struct.pack('b', 10)
		sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

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

		    # Look for responses from all recipients
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
