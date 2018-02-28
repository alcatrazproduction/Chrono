#!/usr/bin/python

import MySQLdb

class db(  ):
	_link 	= None
#	TB_Name = "" from parent is table name

	def __init__(self):
		if self._link == None:
			self._link = MySQLdb.connect("localhost","Chrono","Chrono","Chrono" )
		if self._desc == None:	# init table description, one for all instance
			self._desc = []
		if self._link != None:
			try:
				d = self.getTableDescription()
				for r in d:
					self._desc.append([r[0], r[1]])
			except  Exception as e:
				print(e)
				print( self._desc )
			finally:
				print( self._desc)


	def getDbVersion(self):
		try:
			cursor = self._link.cursor()
			cursor.execute("SELECT VERSION()")
			data = cursor.fetchone()
			cursor.close()
		except:
			data = ""
		finally:
			return data

	def getTableDescription(self,):
		try:
			cursor = self._link.cursor()
			cursor.execute("DESC "+ self.__class__.__name__)
			data = cursor.fetchall()
			cursor.close()
		except:
			data = ""
		finally:
			return data
