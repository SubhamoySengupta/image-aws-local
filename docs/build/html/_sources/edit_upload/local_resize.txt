Compressing and Resizing Images
===============================

Installing Dependencies
-----------------------

Installing libjpeg
^^^^^^^^^^^^^^^^^^^^
Libjpeg is a C library for reading and writing image files. Install it from apt-get ::

	$ sudo apt-get install libjpeg-dev


Install python - pillow 
^^^^^^^^^^^^^^^^^^^^^^^^
Pillow is stable working version of PIL (Python Image Library). Simply install pillow from pip: ::

	$ pip install pillow

.. seealso::

	`Pillow Documentation can be found here`_.

	.. _Pillow Documentation can be found here: http://pillow.readthedocs.org


Get the code
-------------

Download the code from the following `link`_.

.. _link: http://noname.local

The zip package includes: ::
	
	~/root
	  | - /resize	  	
	  |     | - / tweak_pic.py
	  |     | - / input_params.py
	  |     | - / __init__.py
	  | - /resizer.py


Provide Access Paths
----------------------

The following information is stored in a text file and is required by the program at runtime

.. hlist::
	:columns: 1

	* source_path - *absolute path of local storage*

.. note::
	
	Local storage path can be network drive. In this case read the article below to 
	`mount network drives permanently on Ubuntu`_.
	
	.. _mount network drives permanently on Ubuntu: https://wiki.ubuntu.com/MountWindowsSharesPermanently


To add this path simply run: ::
	
	$ python resizer.py configure


Available commands
-------------------

The following commands are available: 

.. hlist::
	:columns: 1

	* **$ python resizer.py run** - *Start resizing files*
	* **$ python resizer.py check** - *Get a list of files which needs to be resized*
	* **$ python resizer.py configure** - *Configure local path*
	* **$ python resizer.py help** - *Show available commands*


Important output files
-----------------------


big_image_list.txt
^^^^^^^^^^^^^^^^^^
This file has the list of all images which must be resized. Images with width or height (or both) greater than 6000 pixels are listed here.
 