import psycopg2


class connect_db():
	def __init__(self):
		self.con = psycopg2.connecct("host=localhost user=postgres password=hyve dbname=ebdb")

	def execute(self, script):
		self.cursor = self.con.cursor()
		self.cursor.execute(script)

	def commit(self):
		try:
			self.cursor.commit()
		except:
			print 'Script was not executed due to errors'
			self.cursor.rollback()
