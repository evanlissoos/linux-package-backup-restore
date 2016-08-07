import subprocess
from random import choice
from pymongo import MongoClient
from config import *

#Evan Lissoos
#6/19/16
#Mongo version

#Function to generate a random string of hex charachters as Unique ID
def genUniqueID():
   return ''.join([choice('0123456789ABCDEF') for x in range(6)])


print "*****************"
print "Welcome to snapshot creator"
print "This program assumes that you already have Puppet and pymongo installed on your computer"
print "If not, please exit the program and install the packages"

#Mongo setup
client = MongoClient(IP)
db = client.linux_back


#Get user choice if they want to maintain current package versions, if not, packages will be up to date
maintain_versions = 2
while(maintain_versions == 2):
	choice = raw_input("For the package list to be kept, would you like to maintain the versions of packages currently installed? (y/n) ")
	if(choice == 'y' or choice == 'Y'):
		maintain_versions = 1
	elif(choice == 'n' or choice == 'N'):
		maintain_versions = 0
	else:
		maintain_versions = 2


#Generate Unique ID then check if ID already exists. Push updates to Mongo
unique_id = genUniqueID()
cursor = db.ids.find()
document = False
for doc in cursor:
	document = doc

if not document:
	print "Error: could not communicate with server, aborting..."
	print "*****************"
	quit()

ids = document.get('ids')

while 1:
	if not unique_id in ids:
		ids.append[unique_id]
		break
	else:
		unique_id = genUniqueID

coll.update_one({"_id" : "57670c925bca6d0db8aee2a6"}, {"$set": {"ids": ids}}, upsert=False)

print "Your unique ID is " + unique_id
print "*****************\n"


#Get packages list and edit if desired by user
proc = subprocess.Popen("puppet resource package", shell=True, stdout=subprocess.PIPE)
out = proc.communicate()[0].split('\n')


#If user does not want to maintain versions, we must modify the manifest to indicate so
if not maintain_versions:
	ENSURE_STATEMENT = "\tensure => 'installed',\n"
	maintain = out
	out = []
	for line in maintain:
		if "ensure" in line:
			out.append(ENSURE_STATEMENT)
		else:
			out.append(line)


#Push new list to Mongo
db.public.insert_one(
	{
		'id' : unique_id,
		'package_list' : out
	}
)