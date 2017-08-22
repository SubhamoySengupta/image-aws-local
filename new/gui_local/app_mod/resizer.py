from __future__ import division
import resize
import os

path = os.path.dirname(os.path.realpath(__file__))


def run_8(console, progress):
	big_image_list = []
	drive = resize.input_params.get_path(path)
	console.emit(2, 'Wait for hours :) We will be Scanning for images')
	console.emit(1, '==============================================')

	big_images = resize.input_params.get_dir_info(console, drive)
	console.emit(2, 'Scan Complete...')
	console.emit(1, '==============================================')
	console.emit(1, 'Total number of images found = ' + str(len(big_images)))
	console.emit(1, 'Analyizing files for big Images..')
	i = 0

	count_real_big_images = 0
	progress_count = 0
	for image_path in big_images:
		i += 1
		console.emit(1, image_path)
		if image_path[image_path.rfind('/'):].split('.')[1] == 'jpg':
			new_image = resize.tweak_pic.image_resizer(drive, image_path)
			console.emit(1, image_path)
			if new_image.WIDTH > 5000:
				console.emit(1, 'Real Big Image --> ' + image_path)
				new_image.resize(image_path)
				big_image_list.append(image_path)
				count_real_big_images += 1
			if new_image.HEIGHT > 5000:
				console.emit(1, 'Real Big Image --> ' + image_path)
				new_image.resize_h(image_path)
				big_image_list.append(image_path)
				count_real_big_images += 1
		progress_count += 1
		if progress_count % (len(big_images) / 100) == 0:
			progress.emit(progress_count / (len(big_images) / 100))

	resize.input_params.save_big_image_list(path, big_image_list)
	console.emit(1, 'Total number big images edited = ' + str(count_real_big_images))
	console.emit(1, '~~The END~~')


def check(console, progress):
	big_image_list = []
	drive = resize.input_params.get_path(path)
	console.emit(2, 'Wait for hours :) We will be Scanning for images')
	console.emit(1, '==============================================')

	big_images = resize.input_params.get_dir_info(console, drive)
	console.emit(2, 'Scan Complete...')
	console.emit(1, '==============================================')
	console.emit(1, 'Total number of images found = ' + str(len(big_images)))
	console.emit(1, '\n Analyizing files for big Images..\n')
	i = 0

	count_real_big_images = 0
	progress_count = 0
	for image_path in big_images:
		i += 1
		console.emit(1, image_path)
		if image_path[image_path.rfind('/'):].split('.')[1] == 'jpg':
			new_image = resize.tweak_pic.image_resizer(drive, image_path)
			if new_image.WIDTH > 5000:
				console.emit(1, 'Real Big Image --> ' + image_path)
				big_image_list.append(image_path)
				print image_path
				count_real_big_images += 1
			if new_image.HEIGHT > 5000:
				console.emit(1, 'Real Big Image --> ' + image_path)
				big_image_list.append(image_path)
				count_real_big_images += 1
		progress_count += 1
		if progress_count % (len(big_images) / 100) == 0:
			progress.emit(progress_count / (len(big_images) / 100))

	resize.input_params.save_big_image_list(path, big_image_list)
	console.emit(1, 'Total number big images edited = ' + str(count_real_big_images))
	console.emit(1, '~~The END~~')


def config():
	resize.input_params.config(path)
