import time
import urllib
import json
import sys
from decimal import *
from termcolor import colored

def __unicode__(self): 
	return unicode(self.last) 
        
data = urllib.urlopen("https://www.bitstamp.net/api/ticker/")
cip = json.load(data)['last'] #cip = change in price

while True:
	i=0
	data = urllib.urlopen("https://www.bitstamp.net/api/ticker/")
	jsond = json.load(data)
	pchange = (Decimal(cip) - Decimal(jsond['last']))/Decimal(cip)
	#sys.stdout.write("\r" + str(pchange))
	if pchange > 0:
		sys.stdout.write("\r" + jsond['last'] + " " + colored(str(pchange),"green") + "% change")
	if pchange == 0:
		sys.stdout.write("\r" + jsond['last'] + " " + colored(str(pchange),"grey") + "% change")
	else:
		sys.stdout.write("\r" + jsond['last'] + " " + colored("-" + str(pchange),"red") + "% change")

	 #To make sure it displays in one line
	sys.stdout.flush()
	time.sleep(2) #To prevent API limits. Set to 2 seconds.
	i+=1