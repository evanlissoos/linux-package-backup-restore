import os
import subprocess
import string

#Evan Lissoos
#4/22/16


print "Welcome to snapshot applier"
print "This program assumes that you already have Puppet and Subversion installed on your computer"
print "If not, please exit the program and install the packages"
print ""

#os.system("svn update")
command = subprocess.Popen("git update", shell=True, stdout=subprocess.PIPE)
outHold = command.communicate()[0]

UNIQUE_ID = raw_input("Please enter your unique ID exactly as it appeared when the snapshot was created: ")

try:
	test_file = open(".snap/" + UNIQUE_ID + ".pp", 'r')

except IOError:
	print "Error: invalid ID"

else:
	test_file.close()
	command = subprocess.Popen("puppet apply " + ".snap/" + UNIQUE_ID + ".pp", shell=True, stdout=subprocess.PIPE)
	outHold = command.communicate()[0]
