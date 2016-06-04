# linux-package-backup-restore

The purpose of this program is to backup and restore all packages installed on any given Linux machine. This program assumes you have both Puppet and Git installed. The program will ask the user if they would like to maintain package versions or not. If they select no, when restoring this list, the most up-to-date version of the packages will be installed.

First, use the create script on a given machine to generate a package list. This will output a unique ID that can be used to restore this backup on any desired client. To restore from a backup, simply clone the repo, install Puppet, then run the apply script and enter the unique ID of the desired restore.

For personal use I reccomend creating your own Git repository with the files found here. This program works by creating package lists and then committing the list to a repository. If you create your own repo, you will be able to store all your backups in a repo.
