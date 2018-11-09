import matplotlib.pyplot as plt
import time
#all functions should take a list as returned by db_temp_builder1.return_table() as a parameter
#ie a list of (int epochtime, int localtemp, int globaltemp, int humidity)

currentdatetime = 'graphall' + time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()) + '.png'

#function that pulls last 24 hours of database, graphs by hours
def graph_lastday(databaselist): #86400 sec in day
	lastdaytemps = []
	for x in databaselist:
		if x[0] < time.time() and x[0] > time.time() - 86400: #should only grab things from db in the last day 
			lastdaytemps.append(x)

	fig=plt.figure() #not sure what this does
	fig.suptitle(currentdatetime, fontsize=14, fontweight='bold')
	plt.axis([0,len(lastdaytemps)+1,0,120]) #declares default values for the graph xmin, xmax and then ymin, ymax
	#plt.ion() # no idea what this does
	ax = fig.add_subplot(111)
	fig.subplots_adjust(top=0.85)
	ax.set_title('Temperatures for ' + currentdatetime)
	ax.set_xlabel('Hour')
	ax.set_ylabel('Temperature F')
	i=0
	while i < len(lastdaytemps):
		plt.scatter(i, lastdaytemps[i][2], label=str(lastdaytemps[i][2]))
		if(i>0): #if this is not the first iteration, draw a line from the last point to the current point
			plt.plot([i-1, i], [lastdaytemps[i-1][2], lastdaytemps[i][2]], 'k-')
		print i, lastdaytemps[i][2]
		i=i+1
	
	fig.savefig(currentdatetime)
	print lastdaytemps
	
#function that pulls last 30 days, graphs high/low by days
#function that pulls all month average high/low, extreme high/low by month


#function that graphs all data, proof of concept
def graph_all(databaselist):
	fig=plt.figure() #not sure what this does
	plt.axis([0,len(databaselist)+1,0,120]) #declares default values for the graph xmin, xmax and then ymin, ymax
	plt.ion() # no idea what this does
	i=0
	print len(databaselist)
	while i < len(databaselist):
		plt.scatter(i, databaselist[i][2], label=str(databaselist[i][2]))
		if(i>0): #if this is not the first iteration, draw a line from the last point to the current point
			plt.plot([i-1, i], [databaselist[i-1][2], databaselist[i][2]], 'k-')
		print i, databaselist[i][2]
		i=i+1

	fig.savefig(currentdatetime)
	
	
	
if __name__ == "__main__":
	listofstuff = [(1, 2, 3, 3), (1480612447.239, 0, 41.5, 81), (1480612462.3, 0, 41.5, 81), (1480616063.75, 0, 42, 81), (1480619665.286, 0, 43.9, 81), (1480623266.86, 0, 43.7, 75), (1480626868.325, 0, 45.8, 75), (1480630469.814, 0, 45.6, 75), (1480634071.264, 0, 45.5, 76), (1480637672.714, 0, 45.8, 81), (1480641274.278, 0, 45.3, 81), (1480644875.743, 0, 46, 87), (1480648477.209, 0, 46.1, 87), (1480652078.678, 0, 45.3, 87), (1480655680.11, 0, 45, 87), (1480659281.536, 0, 44.8, 87), (1480662882.978, 0, 45.1, 81), (1480702151.193, 0, 43.8, 93), (1480702983.357, 0, 43.8, 93), (1480703022.715, 0, 43.8, 93), (1480703095.655, 0, 43.8, 93), (1480703162.966, 0, 43.8, 93), (1480703506.596, 0, 43.8, 93), (1480703584.624, 0, 44.3, 93)]
	#what is this? 20181108
	graph_lastday(listofstuff)
"""
fig=plt.figure() #not sure what this does
maxthroughput = 10
duration = 100
runningtime = 200
plt.axis([0,runningtime,0,1000]) #declares default values for the graph
plt.ion() # no idea what this does
plt.show() #shows the graph
fig.savefig('foo.png')
time.sleep(5)
"""

