from PyQt5 import   QtWidgets
import random

import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow.Ui_MainWindow):
	def __init__(self, parent=None):
		super(MainWindow, self).__init__(parent)
		self.setupUi(self)

	def connectActions(self):
		self.actionQuitter.triggered.connect(QtWidgets.qApp.quit)
		print ( self )

	def main(self):
		self.connectActions()
		self.L_racerlist.setSortingEnabled(True)
		for i in range(1, 10, 1):
			item = QtWidgets.QListWidgetItem()
			item.setText( "racer"+"%10.3f abc" % random.random() )
			self.L_racerlist.addItem(item)
		self.show()
