
from threading 		import Thread
from time 			import time, sleep
import socket
import struct
from random 			import randrange
import Globals

class decoder():
	tp_base		= 1000000
	transponder	= {}
	howmany		= 0

	def createThread(self,d,  decoder, name):

		if self.howmany < decoder['howmany']:
			self.howmany = decoder['howmany']
		i 		= len( self.transponder )
		while len( self.transponder ) < self.howmany:
			self.transponder[self.tp_base+i]		= []
			self.transponder[self.tp_base+i].append(
											int(time()*1000) - randrange( decoder['delay']*1000,  decoder['laptime'] * 1000 )
											)
			self.transponder[self.tp_base+i].append(
			                                        0
											)
			i = i +1
		if  decoder['type'] == 0 and  decoder['auto_assign']:
			print( "Auto assign Transponder activated")
			i = 0
			rl = Globals.MainWindow.L_racerlist
			for c in range( 0,  rl.count()):
				t = rl.item(c).data(Globals.UserRole)
				print( t )
				Globals.racerList[t]['transponder'] = 1000000+i
				i += 1
#				if i > self.howmany:
#					break
		for t in self.transponder:
			tp = self.transponder[t]
			for i in range( len( tp ), decoder['type'] + 2 ):
				tp.append(  tp[1] )
		p = Thread( target=self.decoder, args=(decoder['laptime'],
									    decoder['delay'],
									    d['multi_ip'],
									    d['port'],
									    decoder['type'])
									    )
		return p



	def decoder(self,  laptime, delay,  ip, port,  type):

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
					p_transponder[1000000+i]	= []
					p_transponder[1000000+i].append( tc )
					i = i +1
				t = p_transponder
			else:
				t = self.transponder


			tp		= randrange( self.tp_base, self.tp_base + len( self.transponder ))
			millis	= tc
			if  self.transponder[tp][0] < ( tc + delay ):
				if t[tp][0]  < ( tc  - laptime + delay):
					f = True
					if type == 0:	# finish line
						l = self.transponder[tp][1] + 1
						for i in range( 2, len( self.transponder[tp] ) ):
							if self.transponder[tp][i] < l:
								f = False
					else:
						l = self.transponder[tp][ type + 1] + 1
						for i in range( 2, type + 1 ):
							if self.transponder[tp][i] < l:
								f = False
					if f:
						self.transponder[tp][ type + 1] += 1
						t[tp][0] = tc
						try:
							message = str(tp) +" " + str( millis )
							sock.sendto(message.encode(), multicast_group)
						except socket.timeout:
							print("exception on send multicast")
						finally:
							message=""
			sleep( randrange(50, 1000) / 1000 )
		exit(0)
