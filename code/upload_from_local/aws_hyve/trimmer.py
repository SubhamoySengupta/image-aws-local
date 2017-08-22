import codecs


def trim_file_list(file_name, dest):
	f = codecs.open(file_name, 'r', 'utf-8')
	o = open('out/trimmed.txt', 'w')
	for line in f.readlines():
		if 'Completed ' not in line:
			o.write(line[line.find(dest) + len(dest):])
	f.close()
	o.close()


def check(file_name):
	f = open(file_name, 'r')
	error = []
	success = []
	for line in f.readlines():
		# check1 = Everything smallcaps
		if not line.islower():
			error.append(line)
			continue
		# check2 = heirarchy must be chains/slug/photos/filename.jpg
		sub = line.split('/')
		if len(sub) != 4:
			error.append(line)
			continue
		if not (sub[0] == 'chains' or sub[0] == 'stores'):
			error.append(line)
			continue
		if not(sub[2] == 'menus' or sub[2] == 'photos'):
			error.append(line)
			continue
		# check3 = Filename must be digit
		filename = line[line.rfind('/') + 1:]
		filename, extension = filename.split('.')
		if not filename.isdigit():
			error.append(line)
			continue
		# check4 = extension must be jpg
		if 'jpg' not in extension:
			error.append(line)
			continue
		success.append(line)
	return success, error
