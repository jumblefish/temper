#!/usr/bin/python
import ConfigParser, os, sys, subprocess, string


#should probably make a class for all this
def generate_default_config(): #generates a default config file
    cfgfile = open(os.getcwd() + "/default.cfg",'w')
    Config = ConfigParser.ConfigParser()
    Config.add_section('emailinfo')
    Config.set('emailinfo','sender', 'sdummy1@place.com')
    Config.set('emailinfo','senderpassword', "password")
    Config.set('emailinfo','receiver1', "rdummy1@place.com")
#    Config.set('emailinfo','receiver2', "rdummy2@place.com")
    Config.write(cfgfile)
    cfgfile.close()
    print "default.cfg generated. Quiting..."
    exit()

def pullemailinfo(configfilename):
    #this needs to be reworked to handle multiple emails
    #also reworked into a class
    config = ConfigParser.ConfigParser()
    config.read("./" + configfilename)
    flags = [None]*3
    flags[0] = config.get('emailinfo', 'sender')
    flags[1] = config.get('emailinfo', 'senderpassword')
    flags[2] = config.get('emailinfo', 'receiver1')
    return flags

