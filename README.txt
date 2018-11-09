Script to collect temperature data from the web,
store it in a database, 
draw a graph of the data, 
email the graph.

temperaturecollect.py is the prime script
execution will run indefinitely, collecting data every hour and 
graphing/mailing data one a day
A log is generated

to do:
1. clean up main loop:
	add verbose flag
	restructure loop conditionals
	add functionality so can be run as a cron job instead of a loop
2. add config class
	do not return lists; return class object
	allow for multiple arbritrary recipiants
	integrate with email commands
3. review database command file
4. clean graph generator, create class?

part 2:
add local temp collection
1. recreate usb therm driver
2. set up collection (extend existing methods)


