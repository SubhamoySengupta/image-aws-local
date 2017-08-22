.. Syncing Images for Hyve Application documentation master file, created by
   sphinx-quickstart on Wed May  6 18:43:34 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Hyve App Image Sync's documentation!
===============================================================


This documentation explains the procedures to sync all types of images for **Hyve app**, create copies, create thumbnails, adding watermarks, etc.

*There are two major storage locations of images:*

.. hlist::
	:columns: 1

	* **Local Cloud Storage**
	* **Remote AWS S3-Bucket** - *hyve-rootwork*

.. note::

	Images from various sources are first stored in the **local storage**. These images are raw and require refinements and editing (using Image Editors) which is not discussed in this doc. Other operations like backup and recovery procedures are not mentioned in this doc.

*Images which are displayed in the Hyve app can classified into:*

.. hlist::
	:columns: 1

	* **Looks** - *Looks created by users/others*
	* **Store/Photos** - *Images of stores*
	* **Store/Menus** - *Scanned copies of menus offered by stores*


Contents:

.. toctree::
   :maxdepth: 2
   
   edit_upload/EditingUploading.rst
   sync_buckets/syncing_editing.rst
   gen_sql/script.rst

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
