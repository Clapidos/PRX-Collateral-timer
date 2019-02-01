import time
import requests

print ""
print "*************************************************************"
print "*	Buy me a coffee                                     *"
print "*	Donation Address:PKYrZRgcEDdGcWPCJzwc7m5EsmfGaqpZr7 *"
print "*	Also can be found in the Zipped file as text :D     *"
print "*************************************************************"
print ""
print ""

while True:
	mint=0
	day=0
	hours=0	
	getblock=requests.get("http://178.238.235.79/api/getblockcount")
	a= getblock
	for block in getblock:
		BlockCount=block
		print "**************************"
		print "*  Total Blocks:",BlockCount,"  *"
		print "**************************"
		print ""
	for i in range(int(BlockCount),125000):
		mint=mint+1
		if mint==60:
			hours=hours+1
			mint=0
		
			if hours==24:
				day=day+1
				hours=0
	print "********************************************"
	print "* Blocks until Colateral Increase:",125000-int(BlockCount), "  *"
	print "********************************************"
	print ""
	print "********************************************"
	print "* 	Colateral increase in:~	           *"
	print "*		Days:"+str(day),"	           *"
	print "*		Hours:"+str(hours),"	           *"
	print "*		Minutes:"+str(mint),"	           *"
	print "********************************************"
	print""
	print "Next update in 60 Seconds..."
	time.sleep(60)
