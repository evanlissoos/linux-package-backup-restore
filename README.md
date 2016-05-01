# linux-package-backup-restore

The purpose of this program is to backup and restore all packages installed on any given Linux machine. This program assumes you have both Puppet and Git installed. The program will ask the user if they would like to maintain package versions or not. If they select no, when restoring this list, the most up-to-date version of the packages will be installed.

The way to use this program is by using the create script on a given machine to generate a package list. This will give the user a unique ID that can be used to restore this backup on any desired client. To restore from a backup, simply run the apply script and enter the unique ID of the desired restore.

For personal use I reccomend creating your own Git repository with the files found here. This program works by creating package lists and then committing the list to a repository. If you create your own repo, you will be able to store all your backups in a repo. When you wish to set up a machine with a generated backup, you simply install Git and clone your repo onto the machine.

To generate a package list, use the "create.py" Python script. This will give you a unique ID, make sure you keep note of this.

To apply a backup to a client, use the "apply.py" Python script. This will take in a unique ID and apply all packages found in the list. If you see errors, do not worry that is completely normal. The program is simply trying to install packages that are already installed.
