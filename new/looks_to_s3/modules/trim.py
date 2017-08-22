import urllib
from os import walk


def get_local_look_list(path):
	files = []
	for (dirpath, dirnames, filenames) in walk(path):
		if filenames:
			for file_name in filenames:
				if '.jpg' in file_name:
					files.append(dirpath + '/' + file_name)
	return files


def get_pin_list(path):
	urls = []
	f = open(path + '/out/pin_list', 'r')
	for line in f.readlines():
		urls.append(line)
	return urls


def user_list(user_image_list):
	return_list = {}
	for key in user_image_list:
		key_name = key.name
		dir_id = key_name[:key_name.find('/')]
		w_image = key_name[key_name.find('/') + 1:]
		if '/' in w_image:
			continue
		else:
			if dir_id not in return_list:
				return_list[dir_id] = {}
				return_list[dir_id]['image_list'] = []
			return_list[dir_id]['image_list'].append(w_image)

	return return_list


def read_image(IMAGE_URL, image_name):
	f = open(image_name, 'wb')
	f.write(urllib.urlopen(IMAGE_URL).read())
	f.close()

