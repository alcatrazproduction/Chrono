#!/usr/bin/python

import MySQLdb

class db( MySQLdb ):
	link = None

	def __init__(self):
		self.link = self.connect("localhost","Chrono","Chrono","Chrono" )

	def getDbVersion(self):
		cursor = self.link.cursor()
# execute SQL query using execute() method.
		cursor.execute("SELECT VERSION()")
# Fetch a single row using fetchone() method.
		data = cursor.fetchone()
		cursor.close()
		return data
