from os import walk


def get_path(path):
	f = open(path + '/resize/path.txt', 'r')
	root = ''
	for l in f.readlines():
		root = l[l.find('=') + 1:].strip()
	return root


def get_dir_info(path):
	arr = []
	for (dirpath, dirnames, filenames) in walk(path):
		if filenames:
			for files in filenames:
					arr.append(dirpath + '/' + files)
	return arr


def save_big_image_list(path, big_image_list):
	f = open(path + '/out/big_image_list.txt', 'w')
	for im in big_image_list:
		f.write(im)
		f.write('/n')


def config(path):
	print 'Enter the source path'
	source = raw_input('>')
	if source is '' or '/' not in source:
		print 'Source path doesnot look good! Enter again'
		return
	source = 'source=' + str(source)
	f = open(path + '/resize/path.txt', 'w')
	f.write(source)
	f.close()
