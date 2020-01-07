import mysql.connector

class pyDB():
	DB = ""
	MC = ""
	def __init__(self, Conn, User, Passwd, Database):
		try:
			DB = mysql.connector.connect(host=Conn,
                               user=User,
                               passwd=Passwd,
                               database=Database)
			MC = DB.cursor(buffered=True)
		except mysql.connector.Error as e:
  			print("Something went wrong: {}".format(e))

	def closeConn(self):
		try:
			DB.close()
		except Exception as e:
			print(e)
		
	def fileReadIn(self, fileName):
		Queries = ""
		try:
			f = open(fileName, 'r')
			sf = f.read()
			f.close()
			Queries = sf.split(';')
		except IOError as e:
			print(e)
			return False
		return Queries

	def DDL_DML(self, Query, Values = None):
		try:
			MC.execute(Query, Values)
			DB.commit()
		except mysql.connector.Error as e:
			print(e.msg)
			return False
		return True

	def DQL(self, Query, Values = None, Num = 0):
		Result = ""
		try:
			MC.execute(Query, Values)
			if Num == 0:
				Result = MC.fetchall()
			elif Num == 1:
				Result = MC.fetchmany()
			elif Num == 2:
				Result = MC.fetchone()
		except mysql.connector.Error as e:
			print(e.msg)
			return False
		return Result
