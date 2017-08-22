Syncing local storage and S3 bucket
====================================

Installing Dependencies
-----------------------

AWS CLI Installation
^^^^^^^^^^^^^^^^^^^^
You must install AWS CLI Interface to run aws commands from your terminal. On Ubuntu run: ::

	$ curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-bundle.zip"
	$ unzip awscli-bundle.zip
	$ sudo ./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws

.. seealso::

	`Install the AWS CLI Using the Bundled Installer`_.

	.. _Install the AWS CLI Using the Bundled Installer: http://docs.aws.amazon.com/cli/latest/userguide/installing.html#install-bundle-other-os



Get the code
-------------

Download the code from the following `link`_.

.. _link: http://noname.local

The zip package includes: ::
	
	~/root
	  | - /out
	  | - /sync_module	  	
	  |     | - / cli.py
	  |     | - / paths.py
	  |     | - / __init__.py
	  | - /hyve_sync.py


Provide Access Paths
----------------------

The following information are stored in a text file and are required by the program at runtime

.. hlist::
	:columns: 1

	* source_path - *absolute path of local storage*
	* destination_path - *S3 bucket path*

.. note::
	
	Local storage path can be network drive. In this case read the article below to 
	`mount network drives permanently on Ubuntu`_.
	
	.. _mount network drives permanently on Ubuntu: https://wiki.ubuntu.com/MountWindowsSharesPermanently


To add/edit these paths simply run: ::
	
	$ python hyve_sync.py configure


Available commands
-------------------

The following commands are available: 

.. hlist::
	:columns: 1

	* **$ python hyve_sync.py dryrun** - *Generate a list of files which needs to be updated/copied*
	* **$ python hyve_sync.py copy** - *Start copying the list of files*
	* **$ python hyve_sync.py sync** - *Sync local drive with s3 buckets*
	* **$ python hyve_sync.py configure** - *Configure local and remote paths*
	* **$ python hyve_sync.py help** - *Show available commands*


Important output files
-----------------------


error.txt
^^^^^^^^^^
List of files in local drive which are not uploaded are saved here. Files without an appropiate path, name, or extension are not uploaded.
The following checks ensure that a file will not be copied to remote bucket: 

.. hlist::
	:columns: 1 

	* The path(url) must be of the following format - *stores/{slug_name_of_store}/{photos or menus}/{numerical name}.jpg*
	* File extension must be 'jpg'
	* FileName must be a digit.

This error file must be referred so as to correct the image file properties in the local storage.


success.txt
^^^^^^^^^^^^

The list of files in local drive which are ready to be copied to the remote bucket.

