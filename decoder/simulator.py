
from threading 		import Thread
from time 			import time, sleep
import socket
import struct
from random 			import randrange

class decoder():
	task			= dict()
	tp_base		= 1000000
	transponder	= {}
	howmany		= 0

	def createThread(self,d,  decoder, name):

		if self.howmany < decoder['howmany']:
			self.howmany = decoder['howmany']
		i 		= len( self.transponder )
		while len( self.transponder ) < self.howmany:
			self.transponder[self.tp_base+i]	= int(time()*1000) - randrange( decoder['delay']*1000,  decoder['laptime'] * 1000 )
			i = i +1
		p = Thread( target=self.decoder, args=(decoder['laptime'],
									    decoder['delay'],
									    d['multi_ip'],
									    d['port']))
		return p



	def decoder(self,  laptime, delay,  ip, port):

		if delay > 0:
			p_transponder	= {}
		multicast_group = (ip,port)
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sock.settimeout(0.1)
		ttl = struct.pack('b', 10)
		sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)
		delay 	= delay * 1000
		laptime	= laptime * 1000

		while(1):
			tc = int(time()*1000)
			if delay > 0:
				i = len( p_transponder )
				while len( p_transponder ) < self.howmany:
					p_transponder[1000000+i]	= tc
					i = i +1
				t = p_transponder
			else:
				t = self.transponder


			tp		= randrange( self.tp_base, self.tp_base + len( self.transponder ))
			millis	= tc
			if  self.transponder[tp] < ( tc + delay ):
				if t[tp]  < ( tc  - laptime + delay):
					t[tp] = tc
					try:
						message = str(tp) +" " + str( millis )
						sock.sendto(message.encode(), multicast_group)
					except socket.timeout:
						print("exception on send multicast")
					finally:
						message=""
			sleep( randrange(50, 1000) / 1000 )
		exit(0)
