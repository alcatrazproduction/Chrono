#!/usr/bin/python3 .
######################################################################################
# (c) Yves Huguenin, yves.huguenin@free.fr, mars 2018							#
######################################################################################

import sys
sys.path.append("gui")
sys.path.append("tables")
sys.path.append("decoder")
#from PyQt5 				import  QtWidgets
from PyQt5.QtWidgets		import QApplication
import	Globals


from MainWindow 				import MainWindow
from decoder_task				import decoder_task
from receive					import receive
from Preferences				import Preferences as pref


if __name__=='__main__':

	app = QApplication(sys.argv)
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
