import os
import subprocess
import string
import random

#	Evan Lissoos
#	4/22/16

#Future functionality:
	#We could copy, save, then restore IP Tables
	#http://linux.byexamples.com/archives/66/iptables-rules-can-be-easily-import-and-export/

	#We could also manage specific directories and files


#Function to generate a random string of hex charachters as Unique ID
def genUniqueID():
   return ''.join([random.choice('0123456789ABCDEF') for x in range(6)])


print "Welcome to snapshot creator"
print "This program assumes that you already have Puppet and Subversion installed on your computer"
print "If not, please exit the program and install the packages"
print ""


#Get user choice if they want to maintain current package versions
MAINTAIN_VERSIONS = 2
while(MAINTAIN_VERSIONS == 2):
	CHOICE = raw_input("For the package list to be kept, would you like to maintain the versions of packages already installed? (y/n) ")
	if(CHOICE == 'y' or CHOICE == 'Y'):
		MAINTAIN_VERSIONS = 1
	elif(CHOICE == 'n' or CHOICE == 'N'):
		MAINTAIN_VERSIONS = 0
	else:
		MAINTAIN_VERSIONS = 2


#Generate Unique ID then check if ID already exists
UNIQUE_ID = genUniqueID()
UNIQUE_ID_FOUND = 0
ID_FILE = open(".snap/ids.txt", "r")

while(not(UNIQUE_ID_FOUND)):
	EXISTS = 0

	for line in ID_FILE:
		if UNIQUE_ID in line:
			EXISTS = 1

	if(EXISTS):
		UNIQUE_ID = genUniqueID()
		ID_FILE.seek(0)
	else:
		UNIQUE_ID_FOUND = 1

ID_FILE.close()
ID_FILE = open(".snap/ids.txt", "a")
ID_FILE.write(UNIQUE_ID + "\n")
print "Your unique ID is " + UNIQUE_ID

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

#Add then commit everything to the SVN
commit_message = '"Adding case ID' + UNIQUE_ID + '"'
		
command = subprocess.Popen("git update", shell=True, stdout=subprocess.PIPE)
outHold = command.communicate()[0]
command = subprocess.Popen("git add " + NEW_MANIFEST_NAME, shell=True, stdout=subprocess.PIPE)
outHold = command.communicate()[0]
command = subprocess.Popen("git commit -m " + commit_message, shell=True, stdout=subprocess.PIPE)
outHold = command.communicate()[0]
command = subprocess.Popen("git push -u origin master", shell=True, stdout=subprocess.PIPE)
outHold = command.communicate()[0]
