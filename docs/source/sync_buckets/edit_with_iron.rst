Queue Image Editing task to Iron Worker
=======================================


Installing Dependencies
-----------------------

Installing iron worker CLI
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Iron worker runs tasks in the background, in parallel, and at massive scale. 
to install iron worker ruby cli `refer this link`_.

	.. _refer this link: http://dev.iron.io/worker/reference/cli/



Queueing tasks
---------------
Tasks get queued once copy or sync command is executed.


Description of tasks performed
-------------------------------

.. hlist::
	:columns: 1

	* **Apply company_logo watermark** - For store images watermark are applied at the center of the image. For menu images two watermarks are applied at the top-left and bottom-right corners.
	* **Create multi-size copies** - Calculating image dimensions multiple copies are created to suite different screen size. 
	* **Create a url string based on image_sizes** - A url_string is created comprising all the widths of copied images. A string like '*__w-400-600-800__*' means the original image was copied in three different widths ie: 400, 600, 800 pixels. The aspect ratio is maintained w.r.t the original image.
	* **Save the images in hyve-store** - For a url_string '*__w-400-600-800__*', the following pattern will be followed:
		.. hlist::
			:columns: 1

			* '*../__w-400-600-800__/image_name*' - this is the directory where the image with original dimension are saved

			* '*../w400/image_name*'' - image with width 400 pixels will be saved here.
			
			* '*../w600/image_name*'' - image with width 600 pixels will be saved here.
			
			* '*../w800/image_name*'' - image with width 800 pixels will be saved here.

			* The idea of doing this is that the api will only provide the first url_string to the app, but the app depending on the screen size, available canvas for display, etc, can alter the url and fetch a different image of appropriate size and dimension.