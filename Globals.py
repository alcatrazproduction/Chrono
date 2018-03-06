#All Globals....
from PyQt5.QtGui		import	QFont, QColor

C_concurrents_item_fmt		= "%4.0d %-12.10s %-15.10s"
C_concurrents_moni_fmt		= "%-12.10s %-15.10s"
C_concurrents_ID_fmt			= "ID_%16.16X"
C_concurrents_TP_fmt			= "TP_%8.8X"
# font used in list
C_listFont = QFont()
C_listFont.setFamily("Courier New")
C_listFont.setPointSize(8)
C_listFont.setBold(False)
C_listFont.setItalic(False)
C_listFont.setWeight(50)
C_listFont.setKerning(False)
#
receiver							= {}
decoder							= {}
#
dictBestLapMonitor					= dict()
#dictBestLap						= dict()
dictRace							= dict()
#
clear_screen						= chr(27)+"c"
text_black						= chr(27)+"[30m"
text_red							= chr(27)+"[31m"
text_green						= chr(27)+"[32m"
text_blue							= chr(27)+"[34m"
text_normal						= chr(27)+"[27m"
text_inverted						= chr(27)+"[7m"
max_time							= 0xFFFFFFFF

def createTime( milli):
	second 	= int( ( milli / 1000 ) ) % 60
	minute	= int( ( milli / 1000 / 60 ) ) % 60
	heure	= int( ( milli / 1000 / 3600 ) ) %24
#	days		= int( ( milli / 1000 / 3600 / 24 ) ) %10
	milli		= milli % 1000
	return '{:0d}'.format(heure)+':'+'{:02d}'.format(minute)+':'+'{:02d}'.format(second)+'.'+'{:04d}'.format(milli)

MainWindow						= None
UserRole	 						= 0x0100
racerList 						= {}
tpRacerList						= {}
colorRed							= QColor( 0xff0000 )
colorGreen						= QColor( 0x00ff00 )
colorBlue						= QColor( 0x0000ff )
colorCyan						= QColor( 0x00ffff   )
colorWhite						= QColor( 0xffffff )
