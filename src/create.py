import os
import subprocess
import string
import random
import base64
from pymongo import MongoClient

#Evan Lissoos
#6/19/16
#Mongo version

#Function to generate a random string of hex charachters as Unique ID
def genUniqueID():
   return ''.join([random.choice('0123456789ABCDEF') for x in range(6)])


print "*****************"
print "Welcome to snapshot creator"
print "This program assumes that you already have Puppet and pymongo installed on your computer"
print "If not, please exit the program and install the packages"

#Mongo setup
client = MongoClient(base64.b64decode('ZWMyLTU0LTE5MS0yNDUtMzUudXMtd2VzdC0yLmNvbXB1dGUuYW1hem9uYXdzLmNvbQ=='))
db = client.linux_back


#Get user choice if they want to maintain current package versions, if not, packages will be up to date
MAINTAIN_VERSIONS = 2
while(MAINTAIN_VERSIONS == 2):
	CHOICE = raw_input("For the package list to be kept, would you like to maintain the versions of packages currently installed? (y/n) ")
	if(CHOICE == 'y' or CHOICE == 'Y'):
		MAINTAIN_VERSIONS = 1
	elif(CHOICE == 'n' or CHOICE == 'N'):
		MAINTAIN_VERSIONS = 0
	else:
		MAINTAIN_VERSIONS = 2


#Generate Unique ID then check if ID already exists. Push updates to Mongo
UNIQUE_ID = genUniqueID()
UNIQUE_ID_FOUND = 0
cursor = db.ids.find()
document = 0
for doc in cursor:
	document = doc
IDS = document.get('ids')

while 1:
	if not UNIQUE_ID in IDS:
		IDS.append[UNIQUE_ID]
		break
	else:
		UNIQUE_ID = genUniqueID

coll.update_one({"_id" : "57670c925bca6d0db8aee2a6"}, {"$set": {"ids": IDS}}, upsert=False)

print "Your unique ID is " + UNIQUE_ID
print "*****************\n"


#Get packages list and edit if desired by user
proc = subprocess.Popen("puppet resource package", shell=True, stdout=subprocess.PIPE)
out = proc.communicate()[0].split('\n')


#If user does not want to maintain versions, we must modify the manifest to indicate so
if not MAINTAIN_VERSIONS:
	ENSURE_STATEMENT = "	ensure => 'installed',\n"
	out = []
	for line in split:
		if "ensure" in line:
			out.append(ENSURE_STATEMENT)
		else:
			out.append(line)


#Push new list to Mongo
db.public.insert_one(
	{
		'id' : UNIQUE_ID,
		'package_list' : out
	}
)