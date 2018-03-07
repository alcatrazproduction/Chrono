#!/usr/bin/python3
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

	for dec in pref.decoderList:
		print ( dec )
		if pref.decoderList[ dec ]['active']:
			Globals.decoder[ dec ]		= decoder_task( pref.decoderList[dec],  dec )
	for task in Globals.decoder:
		receive( task )

	app = QApplication(sys.argv)
	Globals.MainWindow = MainWindow()
	Globals.MainWindow.main()
	app.exec_()
