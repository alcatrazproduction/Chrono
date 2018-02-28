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
			if len(self._desc) == 0:
				try:
					d = self.getTableDescription()
					for r in d:
						self._desc.append([r[0], r[1]])
				except  Exception as e:
					print(e)
		self._data = {}
		self.newRecord()
		self._index	= -1

	def newRecord(self):
		for i in self._desc:
			t = i[1].split('(')[0]
			n = i[0]
			if  t=='int' or  t=='bigint':
				self._data[n] = 0
			elif t=='float' or  t=='double' or  t=='real':
				self._data[n] = 0.0
			else:
				self._data[n] = ""
		self._data['id'] = -1

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

	def getRecord(self,  wclause ):
		try:
			cursor = self._link.cursor()
			cursor.execute("SELECT * FROM "+ self.__class__.__name__+" WHERE "+wclause+" LIMIT ,1")
			data = cursor.fetchone()
			cursor.close()
			if data == None:
				self.newRecord()
				return False
			else:
				for i in range( 0, len(data) -1 ):
					self._data[self._desc[i][0]] = data[i]
		except Exception as e:
			print(e)
		return True

	def getNextRecord(self ):
		try:
			cursor = self._link.cursor()
			cursor.execute("SELECT * FROM "+ self.__class__.__name__+" LIMIT %d,1"%(self._index + 1))
			data = cursor.fetchone()
			cursor.close()
			if data == None:
				self.newRecord()
				return False
			else:
				for i in range( 0, len(data) -1 ):
					self._data[self._desc[i][0]] = data[i]
		except Exception as e:
			print(e)
		self._index += 1
		return True

	def getPrevRecord(self ):
		try:
			cursor = self._link.cursor()
			cursor.execute("SELECT * FROM "+ self.__class__.__name__+ " LIMIT %d,1"%(self._index - 1))
			data = cursor.fetchone()
			cursor.close()
			if data == None:
				self.newRecord()
				return False
			else:
				for i in range( 0, len(data) -1 ):
					self._data[self._desc[i][0]] = data[i]
		except Exception as e:
			print(e)
		self._index -= 1
		return True

