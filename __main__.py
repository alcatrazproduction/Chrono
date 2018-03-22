#!/usr/bin/python3 .
######################################################################################
# (c) Yves Huguenin, yves.huguenin@free.fr, mars 2018										#
######################################################################################

import sys
#sys.path.append("gui")													# add the search path for gui 
#sys.path.append("tables")												# add the search path for tables
#sys.path.append("decoder")												# add the search path for decoder
from PyQt5.QtGui 				import QIcon, QPixmap
from PyQt5.QtWidgets			import QApplication, QStyleFactory
from PyQt5.QtCore 				import QSize,  QRect
import	Globals


from gui.MainWindow				import MainWindow
from decoder_task				import decoder_task
from receive					import receive
from Preferences				import Preferences as pref

def main():
	app = QApplication(sys.argv)
	if "Oxygen" in QStyleFactory.keys():
		app.setStyle( QStyleFactory.create("Oxygen") )					# try to set the Oxygen style
	elif "Fusion" in QStyleFactory.keys():								# if not the try Fusion
		app.setStyle( QStyleFactory.create("Fusion") )

	Globals.icons["finish flag"].addPixmap( QPixmap("Ressources/icons/finish_flag.png"), QIcon.Disabled, QIcon.On)
	Globals.MainWindow = MainWindow()
	Globals.Screen = app.primaryScreen()
	taille 	= Globals.Screen.size()
	height	= taille.height()
	width	= taille.width()
	if False:
		Globals.MainWindow.setMaximumSize( taille )
		Globals.MainWindow.resize( height,  width )
		Globals.MainWindow.Tab_Container.setMaximumSize(QSize( height , width - 40))
		Globals.MainWindow.Tab_Container.setGeometry( QRect(0, 0, height, width - 40))
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
