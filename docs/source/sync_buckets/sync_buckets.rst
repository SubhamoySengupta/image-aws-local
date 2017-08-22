Syncing Hyve-rootwork and Hyve-store buckets
============================================

Installing Dependencies
------------------------

Installing python-boto
^^^^^^^^^^^^^^^^^^^^^^
boto is an integrated python interface to current and future infrastructural services offered by Amazon Web Services.

You can install boto from pip ::

	sudo pip install boto

.. seealso::

	`Getting Started wth boto`_.

	.. _Getting Started wth boto: https://boto.readthedocs.org/en/latest/getting_started.html

Get the code
-------------

Download the code from the following `link`_.

.. _link: http://noname.local

The zip package includes: ::
	
	~/root
	  | - /out
	  | - /resources
	  | - /sync_modules	  	
	  |     | - / aws_con.py
	  |     | - / trim.py
	  |     | - / credentials.py
	  |     | - / __init__.py
	  | - /sync_remote.py
	  | - /iron.json

.. note::
	The iron.json file stores the encrypted token required to invoke iron worker commands


Provide Access Paths and aws credentials
-----------------------------------------

The following information are stored in a text file and are required by the program at runtime

.. hlist::
	:columns: 1

	* **aws_access_key_id**
	* **aws_secret_access_key**
	* **region**
	* **in_bucket**
	* **out_bucket**


To add/edit these information simply run: ::
	
	$ python sync_remote.py configure


Available commands
-------------------

The following commands are available: 

.. hlist::
	:columns: 1

	* **$ python sync_remote.py dryrun** - *Generate a list of files which needs to be updated/copied*
	* **$ python sync_remote.py copy** - *Start copying the list of files*
	* **$ python sync_remote.py sync** - *Sync hyve-rootwork and hyve-store*
	* **$ python sync_remote.py configure** - *Configure aws credentials and in/out buckets*
	* **$ python sync_remote.py help** - *Show available commands*



Important output files
-----------------------


modified.txt
^^^^^^^^^^^^

List of files which exists in hyve-store but needs to be modified.
The following check ensure that a file should be modified in hyve-store bucket: 

.. hlist::
	:columns: 1 

	* the '*last_modified*' property of aws key object tells us the time when a file was last modified in s3 bucket. In any situation the last_modified timestamp of an image file in hyve-rootwork bucket must be older than the timestamp of the corresponding file in hyve-store.


.. note::
	
	Modifying files donot change their url. So no changes are required in the api or the database.


duplicate_stores.txt
^^^^^^^^^^^^^^^^^^^^

List of files which must be deleted from hyve-store since they are no longer required


new.txt
^^^^^^^

The list of files which doesn't exist in hyve-store and needs to be copied.
