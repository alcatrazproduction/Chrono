import socket
import struct

def createTime( milli):
	second 	=  ( milli / 4000 ) % 60
	minute	= ( milli / 4000 / 60 ) % 60
	heure		= ( milli / 4000 / 3600 )
	milli		= milli % 4000
	return '{:0d}'.format(heure)+':'+'{:02d}'.format(minute)+':'+'{:02d}'.format(second)+'.'+'{:04d}'.format(milli)

multicast_group = '224.3.29.71'
server_address = ('', 10000)

# Create the socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind to the server address
sock.bind(server_address)

# Tell the operating system to add the socket to the multicast group
# on all interfaces.
group = socket.inet_aton(multicast_group)
mreq = struct.pack('4sL', group, socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

tplist		= {}

# Receive/respond loop
while True:

	data, address = sock.recvfrom(1024)

	tp		= int( data[:data.find(" ")])
	millis	= int( data[data.find(" "):])
	lap	= 0
	i 		= 0
	rt		= "    Record "

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
	except  ValueError:
		print("got an error")
	finally:
		print ("transponder id: {: 10d}".format( tp ) +", timecode {: 20d}".format( millis ) +", lap time = "+ createTime( lap )  + " -> "+rt+" " +createTime( tplist[tp][1]) )
