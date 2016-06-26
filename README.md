# linux-package-backup-restore

This program is a utility to backup and restore all installed Linux packages on a given machine.

The dependencies for this program are pymongo and Puppet.
	To install Puppet, use your system's package manager.
	To install pymongo, use `pip install`.

To create a backup, run `bin/backup` and you will be given a unique ID. To restore, run `sudo bin/restore` and enter in your ID.

NOTE: If you see errors when restoring from a backup, this is completely normal, just ignore them.
