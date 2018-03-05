#!/usr/bin/python
import sys
sys.path.append("gui/")
sys.path.append("tables")
#from PyQt5 				import  QtWidgets
from PyQt5.QtWidgets		import QApplication
import	Globals


from MainWindow 				import MainWindow
from decoder_task			import decoder_task
from receive					import receive
from Preferences				import Preferences as pref


if __name__=='__main__':

	Globals.decoder		= decoder_task( pref.defaultSerialDevice )
	Globals.receiver		= receive( Globals.decoder.task[ pref.defaultSerialDevice ]['port'])

	app = QApplication(sys.argv)
	Globals.MainWindow = MainWindow()
	Globals.MainWindow.main()
	app.exec_()
