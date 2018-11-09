#!/usr/bin/python


import smtplib
import configfunctions #todo

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
#need to replace config list with class 
maillist = configfunctions.pullmailinfo("default.cfg")
sender = maillist[0]
senderpassword = maillist[1]
rec = maillist[2]

server.login(sender, senderpassword)

message = """From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
MIME-Version: 1.0
Content-type: text/html
Subject: SMTP HTML e-mail test

This is an e-mail message to be sent in HTML format

<b>This is HTML message.</b>
<h1>This is headline.</h1>
"""
msg = "\nHello!" # The /n separates the message from the headers (which we ignore for this example)
#also need to replace these with variables
server.sendmail(sender, rec, message)

print "sent"




