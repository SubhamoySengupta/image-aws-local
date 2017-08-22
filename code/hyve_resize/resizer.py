import resize


def run_8():
	print 'Wait for hours! We are Scanning for big images'

	big_images = resize.input_params.get_dir_info('/run/user/1000/gvfs/smb-share:server=wdmycloud,share=hyve/hyve-rootwork/')
	print 'Total number of images = ', len(big_images)

	i = 0

	count_real_big_images = 0

	for image_path in big_images:
		i += 1
		# print  str(i/len(big_images) *100), " % Complete"
		if image_path[image_path.rfind('/'):].split('.')[1] == 'jpg':
			new_image = resize.tweak_pic.image_resizer(image_path)
			if new_image.WIDTH > 6000:
				print 'Real Big Image --> ', image_path
				new_image.resize(image_path)
				count_real_big_images += 1
			if new_image.HEIGHT > 6000:
				print 'Real Big Image --> ', image_path
				new_image.resize_h(image_path)
				count_real_big_images += 1

	print 'Total number og images edited = ', count_real_big_images
	print '~~The END~~'
