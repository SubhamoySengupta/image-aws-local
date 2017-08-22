import resize
import sys
import os

path = os.path.dirname(os.path.realpath(__file__))


def task(arg):
	if len(arg) > 1:
		options = dict(run=run_8, check=check, help=help, configure=config)
		options[arg[1]]()
	else:
		print '****No arguements given. For help, type --> hyve_sync.py help'


def run_8():
	drive = resize.input_params.get_path(path)
	print 'Wait for hours! We are Scanning for big images'
	big_images = resize.input_params.get_dir_info(drive)
	print 'Total number of images = ', len(big_images)

	i = 0

	count_real_big_images = 0

	for image_path in big_images:
		i += 1
		if image_path[image_path.rfind('/'):].split('.')[1] == 'jpg':
			new_image = resize.tweak_pic.image_resizer(drive, image_path)
			if new_image.WIDTH > 6000:
				print 'Real Big Image --> ', image_path
				new_image.resize(image_path)
				count_real_big_images += 1
				continue
			if new_image.HEIGHT > 6000:
				print 'Real Big Image --> ', image_path
				new_image.resize_h(image_path)
				count_real_big_images += 1

	print 'Total number og images edited = ', count_real_big_images
	print '~~The END~~'


def check():
	big_image_list = []
	drive = resize.input_params.get_path(path)
	print 'Wait for hours! We are Scanning for big images'
	big_images = resize.input_params.get_dir_info(drive)
	print 'Total number of images = ', len(big_images)

	i = 0

	count_real_big_images = 0

	for image_path in big_images:
		i += 1
		if image_path[image_path.rfind('/'):].split('.')[1] == 'jpg':
			new_image = resize.tweak_pic.image_resizer(drive, image_path)
			if new_image.WIDTH > 6000:
				print 'Real Big Image --> ', image_path
				big_image_list.append(image_path)
				count_real_big_images += 1
				continue
			if new_image.HEIGHT > 6000:
				print 'Real Big Image --> ', image_path
				big_image_list.append(image_path)
				count_real_big_images += 1

	resize.input_params.save_big_image_list(big_image_list)
	print 'Total number og images edited = ', count_real_big_images
	print '~~The END~~'


def help():
	print '''\n\t\t\tOptions
=========================================================

run : Starts resizing files

check : Gets a list of files which needs to be resized

configure : Configures local path

help : displays these options :)
'''


def config():
	resize.input_params.config(path)


if __name__ == '__main__':
	task(sys.argv)
