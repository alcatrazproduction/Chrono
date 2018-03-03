#!/usr/bin/python

from PyQt5 				import  QtWidgets
import sys
from MainWindow 		import MainWindow
from decoder_task	import decoder_task

def_ser	= "/dev/ttyUSB0"

if __name__=='__main__':
	decoder	= decoder_task( def_ser )
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = MainWindow()
	MainWindow.main()
	app.exec_()
