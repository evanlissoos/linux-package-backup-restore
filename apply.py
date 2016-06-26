import os
import subprocess
import string

#Evan Lissoos
#4/22/16
#Git Version

os.system("clear")

print "Welcome to snapshot applier"
print "\nPLEASE EXECUTE THIS PROGRAM AS ROOT OR IT WILL FAIL\n"
print "This program assumes that you already have Puppet and Git installed on your computer"
print "If not, please exit the program and install the packages"

CONTINUE = raw_input("Press enter to continue")

os.system("git pull")
os.system("clear")

UNIQUE_ID = raw_input("Please enter your unique ID exactly as it appeared when the snapshot was created: ")

try:
	test_file = open(".snap/" + UNIQUE_ID + ".pp", 'r')

except IOError:
	print "Error: invalid ID\n"

else:
	test_file.close()
	os.system("puppet apply " + ".snap/" + UNIQUE_ID + ".pp")
