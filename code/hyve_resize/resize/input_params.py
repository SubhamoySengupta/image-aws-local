from os import walk


def get_dir_info(path):
	arr = []
	for (dirpath, dirnames, filenames) in walk(path):
		if filenames:
			for files in filenames:
					arr.append(dirpath + '/' + files)
	return arr
