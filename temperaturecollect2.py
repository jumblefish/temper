import sys
import datetime
import time
import db_temp_builder1
import globalweather
import genericgrapher1

startdatetime = datetime.datetime.now()
counter = startdatetime.hour
currentmonth = datetime.datetime.now()
indoortemp = 0
logname = 'log' + time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()) + '.txt'
logfile = open(logname, 'w')

while 1:

	if datetime.datetime.now().day == 1 and currentmonth.month != datetime.datetime.now().month:
		#pull database data 
		#make graph of data for month
		#email to me 
		currentmonth = datetime.datetime.now()
		print "new month", datetime.datetime.now()
		logfile.write("new month" + time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()) + " " + str(counter))
	if datetime.datetime.now().hour == counter:
		#get local temperature
		
		portlandtemp = globalweather.pullglobaltemperature()#get gloabl temperature
		portlandhumidity = globalweather.pullglobalhumidity()#get gloabl hum
		
		db_temp_builder1.addtemp(time.time(), indoortemp, portlandtemp, portlandhumidity) #store in database, date is stored in posix time, use datetime.datetime.fromtimestamp(x) to convert back
		counter = counter + 1
		print "new hour", datetime.datetime.now(), counter
		logfile.write("new hour" + time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()) + " " + str(counter))
	else:
		time.sleep(600) #this will be 3600 at launch
		logfile.write("sleep " + str(counter))

	if datetime.datetime.now().hour == 0 and counter >= 23:
		counter = 0
		
		entirehistory = db_temp_builder1.return_table() #pull database data #probably mod this to only return last day? merge with genericgrapher1.py?
		 
		genericgrapher1.graph_lastday(entirehistory) #make graph of database for day
		#email to me
		print "new day", datetime.datetime.now(), counter
		logfile.write("new day" + time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()) + " " + str(counter))
