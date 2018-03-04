#!/usr/bin/python

#from PyQt5 				import  QtWidgets
from PyQt5.QtWidgets		import QApplication
import	Globals

import sys
from MainWindow 				import MainWindow
from decoder_task			import decoder_task
from receive					import receive
def_ser	= "/dev/ttyUSB0"

if __name__=='__main__':
	sys.path.append("gui/")
	sys.path.append("tables")
	Globals.decoder		= decoder_task( def_ser )
	Globals.receiver		= receive( Globals.decoder.task[def_ser]['port'])

	app = QApplication(sys.argv)
	MainWindow = MainWindow()
	MainWindow.main()
	app.exec_()
