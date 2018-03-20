#!/usr/bin/python3 .
######################################################################################
# (c) Yves Huguenin, yves.huguenin@free.fr, mars 2018							#
######################################################################################

import sys
sys.path.append("gui")
sys.path.append("tables")
sys.path.append("decoder")
from PyQt5.QtGui 				import QIcon, QPixmap
from PyQt5.QtWidgets			import QApplication
import	Globals


from MainWindow 				import MainWindow
from decoder_task				import decoder_task
from receive					import receive
from Preferences				import Preferences as pref

def main():
	app = QApplication(sys.argv)
	Globals.icons["finish flag"].addPixmap( QPixmap("Ressources/icons/finish_flag.png"), QIcon.Disabled, QIcon.On)
	Globals.MainWindow = MainWindow()
	Globals.MainWindow.main()
# Init Decoder interface
	for dec in pref.decoderList:
		print ( dec )
		if pref.decoderList[ dec ]['active']:
			decoder_task( pref.decoderList[dec],  dec )
	for task in Globals.decoder:
		receive( task )
	app.exec_()

if __name__=='__main__':
	main()
