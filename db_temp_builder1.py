import sqlite3

databasename = 'tempstorage.sqlite' #need to implement this

def runsql(sqlcommand):
	print sqlcommand
	conn = sqlite3.connect('tempstorage.sqlite')
	cur = conn.cursor()
	cur.execute(sqlcommand)
	conn.close()
	
def addtemp(m, n, o, p):
	conn = sqlite3.connect('tempstorage.sqlite')
	cur = conn.cursor()
	cur.execute('INSERT INTO Temps (date_time, indoor_temp, outdoor_temp, hum) VALUES (?, ?, ?, ?)', (m, n, o, p))
	conn.commit()
	conn.close()

def print_table():
	conn = sqlite3.connect('tempstorage.sqlite')
	cur = conn.cursor()
	cur.execute('SELECT date_time, indoor_temp, outdoor_temp, hum FROM Temps')
	for row in cur:
		print(row)
	conn.close()

def return_table():
	listoftable = []
	conn = sqlite3.connect('tempstorage.sqlite')
	cur = conn.cursor()
	cur.execute('SELECT date_time, indoor_temp, outdoor_temp, hum FROM Temps')
	for row in cur:
		listoftable.append(row)
	conn.close()
	return listoftable #returns a list of lists, access via x[i][j]
	
def pull_datetimes():
	conn = sqlite3.connect('tempstorage.sqlite')
	cur = conn.cursor()
	cur.execute('SELECT date_time FROM Temps')
	return cur #this returns the database handle. not useful
	
def get_temp(datetime):
	conn = sqlite3.connect('tempstorage.sqlite')
	cur = conn.cursor()
	cur.execute('SELECT indoor_temp FROM Temps WHERE date_time = ?', (str(datetime)))
	#print cur.fetchone()
	return cur.fetchone()
	
if __name__ == "__main__":
	conn = sqlite3.connect('tempstorage.sqlite') #C:\Users\Cylance7\Documents\pythonscripts\
	cur = conn.cursor()
	print "this wipes the current table! cannot be undone Continue? y/n "
	#answer = input("this wipes the current table! cannot be undone Continue y/n?")
	answer = raw_input()
	if answer == 'y':
		cur.execute("DROP TABLE IF EXISTS Temps")
		cur.execute('CREATE TABLE Temps (date_time INTEGER, indoor_temp INTEGER, outdoor_temp INTEGER, hum INTEGER)')
		#conn.close()
		#addtemp(1, 2, 3, 3)
		print_table()
		print "here"
		conn.close()
	else: 
		conn.close()
		print "else"
