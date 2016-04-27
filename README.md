# linux-package-backup-restore

The purpose of this program is to generate a list of all installed packages. You will be given the option to maintain the current version of packages installed or not. If you choose to not maintain the current version, all packages installed on clients will be up to date.

To generate a package list, use the "create.py" Python script. This will give you a unique ID, make sure you keep note of this.

To apply a package list to a client, use the "apply.py" Python script. This will take in a unique ID and apply all packages found in the list. If you see errors, do not worry that is normal. These are just system packages that are already installed or are not needed.
