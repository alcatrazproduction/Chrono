#
# Will send the data on the quenes
#


from threading 		import Thread
from Queue 			import Queue
from time			import time

import socket
import struct
#import Globals

class tpEvent(  ) :
	pos	= None
	tp		= None
	millis	= None
	tc		= None

	def __init__(self, _tp, _time):
		self.tp		= _tp
		self.millis		= _time

class receive:
	task			= dict([])
	soc_ip		= "224.3.29.71"
	soc_port		= 10000
	basems		= 0

	def createTime( self, milli):
		second 	=  ( milli / 4000 ) % 60
		minute	= ( milli / 4000 / 60 ) % 60
		heure		= ( milli / 4000 / 3600 )
		milli		= milli % 4000
		return '{:0d}'.format(heure)+':'+'{:02d}'.format(minute)+':'+'{:02d}'.format(second)+'.'+'{:04d}'.format(milli)


	def __init__(self, port):
		print( port )
		try:
			d = self.task[ port ]
			print( "Allready Open, Sorry")
			return
		except:

			d								= dict()
			d['ip']						= self.soc_ip
			d['port']					= port
			d['queue']					= dict()
			d['queue']['monitor']	= Queue(maxsize=0)
			p = Thread( target=self.receive_task, args=( d['ip'], d['port'],  d['queue']) )
			d['pid']			= p
			self.task[port]	= d
			p.setDaemon(True)
			p.start()

	def receive_task(self, ip, port, queues):
		server_address = ('', port)

# Create the socket
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind to the server address
		sock.bind(server_address)

# Tell the operating system to add the socket to the multicast group
# on all interfaces.
		group = socket.inet_aton( ip )
		mreq = struct.pack('4sL', group, socket.INADDR_ANY)
		sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

		tplist		= {}

# Receive/respond loop
		while True:

			data, address = sock.recvfrom(1024)
			if self.basems	== 0:
				self.basems	= int(time()*1000)  - int( data[data.find(" "):])
			tp		= int( data[:data.find(" ")])
			millis	= int( data[data.find(" "):])
			lap	= 0
#			rt		= "    Record "
			event		= tpEvent( tp, millis + self.basems )
			for q in queues:
				queues[q].put( event )

			try:
				if tp in tplist:
					lap		= millis - tplist[tp][0]
					tplist[tp][0]	= millis
					if lap < tplist[tp][1]:
						tplist[tp][1] = lap
#						rt = "New Record!"
				else:
						tplist.setdefault(tp, [])
						tplist[tp].append( millis )
						tplist[tp].append( 123456789 )
			except  ValueError:
				print("got an error")
#			finally:
#				print ("transponder id: {: 10d}".format( tp ) +", timecode {: 20d}".format( millis ) +", lap time = "+ Globals.createTime( lap )  + " -> "+rt+" " +Globals.createTime( tplist[tp][1]) )
