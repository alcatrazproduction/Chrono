from PyQt5 import  QtWidgets
import sys
from MainWindow import MainWindow

if __name__=='__main__':
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = MainWindow()
	MainWindow.main()
	app.exec_()
