from config import config_database
import mysql.connector

database_config = config_database.config()
class Connection:
	def __init__(self):
		try:
			self.conect =  mysql.connector.connect(**database_config)
			self.cursor = self.conect.cursor(dictionary=True)
		except Exception as e:
			self.connect.close()
			return None

	def query(self, query):
		try:
			self.cursor.execute(query)
			return self.cursor.fetchall()
		except Exception as e:
			print(e)
			return None
		finally:
			self.cursor.close()
