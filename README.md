# linux-package-backup-restore

This program is a utility to backup and restore all installed Linux packages on a given machine.

The dependencies for this program are pymongo and Puppet.
	To install Puppet, use your system's package manager.
	To install pymongo, use pip.

To create a backup, run './backup' and you will be given a unique ID. To restore, call 'sudo ./restore' and enter in your ID.