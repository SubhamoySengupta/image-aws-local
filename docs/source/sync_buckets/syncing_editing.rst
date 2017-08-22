Syncing s3 buckets and editing Images
======================================

These scripts are run from the remote server. In the first stage we compare the two buckets hyve-rootwork and hyve-store to find the list of files we need to copy, modify or delete. In the second stage we queue the image editing tasks in more powerfual and fast IAAS. 

.. toctree::
   :maxdepth: 2

   sync_buckets.rst
   edit_with_iron.rst

