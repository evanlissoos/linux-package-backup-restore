import os
import subprocess
import string
from pymongo import MongoClient

#Evan Lissoos
#6/19/16
#Mongo version

print "*****************"
print "Welcome to snapshot applier"
print "This program assumes that you already have Puppet and pymongo installed on this machine"
print "If not, please exit the program and install the packages using 'pip install'"
print "Also, please execute this program as root otherwise the execution will fail.\n"

UNIQUE_ID = raw_input("Please enter your unique ID exactly as it appeared when the snapshot was created: ")

#Mongo setup
client = MongoClient()
db = client.linux_back
cursor = db.public.find("id" : UNIQUE_ID)


#Retrieve document from Mongo
document = False
for doc in cursor:
	document = doc


#Error if couldn't find the document with the associated ID
if not document:
	print "Error: invalid ID"
	print "*****************"


#Move the package list to a file then apply it with Puppet
else:
	print "*****************"
	packages = document['package_list']
	fileName = 'packages_'+UNIQUE_ID+'.pp'
	for line in packages
		with open(fileName, 'a') as pp:
			pp.write(line+'\n')

	proc = subprocess.Popen('puppet apply ' + fileName, shell=True, stdout=subprocess.PIPE)

	if proc.communicate()[1] == 0:
		print '\nPackage restore has successfully been completed'

	subprocess.Popen('puppet apply ' + fileName, shell=True, stdout=subprocess.PIPE)