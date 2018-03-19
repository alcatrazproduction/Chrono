#!/usr/bin/python
######################################################################################
# (c) Yves Huguenin, yves.huguenin@free.fr, mars 2018							#
######################################################################################
# interface to database tables											#
######################################################################################

import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb

from time				import time
from Preferences		import Preferences as pref

class db(  ):
	_link 		= None												# link to the database. globals to all tables
	flag_local	= (1<<70)												# bit 70 is set, to get local id

	def __init__(self):													# TODO: abstrac the database driver, to be independent
		if self._link == None:											# if no link to database
			self._link = MySQLdb.connect(									# try to open a connection to the database
							pref.dataBase['host'],						# hostname from preference
							pref.dataBase['user'],						# database username
							pref.dataBase['pass'],						# database password
							pref.dataBase['db'],						# database to use
							charset='utf8'								# charset must be utf8
							)
		if self._desc == None:	# init table description, one for all instance
			self._desc = []
		if self._link != None:
			if len(self._desc) == 0:
				try:
					d = self.getTableDescription()
					for r in d:
						self._desc.append([r[0], r[1]])
				except  Exception as e:
					print("ERROR: Getting the table descriptio")
					print(e)
		else:
			print("Error openning dataBase")
			exit( -1 )
		self._data = {}												# initialise the dictionary space
		self.newRecord()												# create all fields
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
		self._data['id'] 	= -1											# if id is negative, record not in database
		self.localid		= int( time() * 1e7) + self.flag_local				# create a local id
		self.modified		= False										# True if record modified
		self.indb			= False										# true if record is in Db

	def getDbVersion(self):												# retrun the database version, may only run on mySql
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

	def getRecord(self,  wclause,  index = 0 ):
		try:
			cursor = self._link.cursor()
			cursor.execute("SELECT * FROM "+ self.__class__.__name__+" WHERE "+wclause+" LIMIT %d,1"%(index ))
			data = cursor.fetchone()
			cursor.close()
			if data == None:
				self.newRecord()
				print("SELECT * FROM "+ self.__class__.__name__+" WHERE "+wclause+" LIMIT %d,1"%(index ))
				return False
			else:
				for i in range( 0, len(data) -1 ):
					self._data[self._desc[i][0]] = data[i]
		except Exception as e:
			print(e)
			return False
		self.indb		= True
		self.modified	= False
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
				for i in range( 0, len(data)  ):
					self._data[self._desc[i][0]] = data[i]
		except Exception as e:
			print(e)
			return False
		self._index += 1
		self.indb		= True
		self.modified	= False
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
			return False
		self._index -= 1
		self.indb		= True
		self.modified	= False
		return True

	def saveRecord( self ):										# TODO: Wrtie the rotine to save the data to database
		return False
		try:
			cursor = self._link.cursor()
			cursor.execute("SELECT * FROM "+ self.__class__.__name__)
			data = cursor.fetchone()
			cursor.close()
			if data == None:
				self.newRecord()
				print("SELECT * FROM "+ self.__class__.__name__)
				return False
			else:
				for i in range( 0, len(data) -1 ):
					self._data[self._desc[i][0]] = data[i]
		except Exception as e:
			print(e)
			return False
		self.indb		= True
		self.modified	= False
		return True
