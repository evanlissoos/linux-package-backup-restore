import os
import subprocess
import string
import random
from pymongo import MongoClient

#Evan Lissoos
#6/19/16
#Mongo version

#Future functionality:
	#We could copy, save, then restore IP Tables
	#http://linux.byexamples.com/archives/66/iptables-rules-can-be-easily-import-and-export/

	#We could also manage specific directories and files

	#Multithread the Puppet installation by splitting up the manifest


#Function to generate a random string of hex charachters as Unique ID
def genUniqueID():
   return ''.join([random.choice('0123456789ABCDEF') for x in range(6)])

print "*****************"
print "Welcome to snapshot creator"
print "This program assumes that you already have Puppet installed on your computer"
print "If not, please exit the program and install the packages"


client = MongoClient()
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


#Generate Unique ID then check if ID already exists
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

#If user does not want to maintain versions, we must modify the manifest to indicate so
if(MAINTAIN_VERSIONS):
	NEW_MANIFEST_NAME = ".snap/" + UNIQUE_ID + ".pp"
	os.system("touch " + NEW_MANIFEST_NAME)
	listPackagesCommand = subprocess.Popen("puppet resource package > " + NEW_MANIFEST_NAME, shell=True, stdout=subprocess.PIPE)

else:
	OLD_MANIFEST_NAME = ".snap/" + UNIQUE_ID + "old.pp"
	NEW_MANIFEST_NAME = ".snap/" + UNIQUE_ID + ".pp"
	os.system("touch " + OLD_MANIFEST_NAME)
	#listPackagesCommand = subprocess.Popen("puppet resource package > " + OLD_MANIFEST_NAME, shell=True, stdout=subprocess.PIPE)
	os.system("puppet resource package > " + OLD_MANIFEST_NAME)

	#Replace 'version number' with 'installed' in manifest file
	ENSURE_STATEMENT = "	ensure => 'installed',\n"

	with open(OLD_MANIFEST_NAME, 'r') as old_manifest:
		with open(NEW_MANIFEST_NAME, 'a') as new_manifest:
			for line in old_manifest:
				if "ensure" in line:
					new_manifest.write(ENSURE_STATEMENT)
				else:
					new_manifest.write(line)

	os.system("rm " + OLD_MANIFEST_NAME)

with open (NEW_MANIFEST_NAME, "r") as myfile:
	data=myfile.readlines()

os.system("rm " + NEW_MANIFEST_NAME)

db[i].insert_one(
	{
		'id' : UNIQUE_ID,
		'package_list' : data
	}
)