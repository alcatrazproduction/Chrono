#!/usr/bin/python3 .
######################################################################################
# (c) Yves Huguenin, yves.huguenin@free.fr, mars 2018							#
######################################################################################
#
# Will send the data on the queues
#


from threading 		import Thread
from queue 			import Queue
from time				import time

import socket
import struct
import Globals

class tpEvent(  ) :
	pos		= None
	tp		= None
	millis	= None
	tc		= None
	type		= None

	def __init__(self, _tp, _time,  _type, _tc, _pos):
		self.pos		= _pos
		self.tp		= _tp
		self.millis	= _time
		self.tc		= _tc
		self.type		= _type

class receive:
	soc_ip		= "224.3.29.71"
	basems		= 0

	def __init__(self, name):
		port = Globals.decoder[ name ]['port']
		try:
			d = Globals.receiver[ name ]
			print( "Allready Open, Sorry(%s:%d)"%(name, port))
			return
		except:

			d						= dict()
			d['ip']					= self.soc_ip
			d['port']					= port
			d['queue']				= dict()
			d['queue']['monitor']		= Queue(maxsize=0)
			p = Thread( target=self.receive_task, args=( d['ip'], d['port'],  d['queue'], Globals.decoder[ name ]['preferences']['type'] ) )
			d['pid']					= p
			Globals.receiver[name]		= d
			p.setDaemon(True)
			p.start()

	def receive_task(self, ip, port, queues, type):
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
			data = data.decode()
			if self.basems	== 0:
				self.basems	= int(time()*1000)  - int( data[data.find(" "):])
			tp		= int( data[:data.find(" ")])
			millis	= int( data[data.find(" "):])
			lap	= 0
			rt		= "    Record "
			event		= tpEvent( tp, millis + self.basems,  type, millis, port )
			for q in queues:
				queues[q].put( event )

			try:
				if tp in tplist:
					lap		= millis - tplist[tp][0]
					tplist[tp][0]	= millis
					if lap < tplist[tp][1]:
						tplist[tp][1] = lap
						rt = "New Record!"
				else:
						tplist.setdefault(tp, [])
						tplist[tp].append( millis )
						tplist[tp].append( 123456789 )
			except  Exception as e:
				print("got an exception")
				print( e )
			finally:
				if False:
					print ("transponder id: {: 10d}".format( tp ) +", timecode {: 20d}".format( millis ) +", lap time = "+ Globals.createTime( lap )  + " -> "+rt+" " +Globals.createTime( tplist[tp][1]) )
