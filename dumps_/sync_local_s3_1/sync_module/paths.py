

def get_path(path):
	f = open(path + '/out/source.txt', 'r')
	source = None
	destination = None
	for line in f.readlines():
		if 'source=' in line:
			source = line[line.find('=') + 1:].strip()
		elif 'destination=' in line:
			destination = line[line.find('=') + 1:].strip()
	return source, destination


def update(path):
	print 'Enter the source path'
	source = raw_input('>')
	print 'Enter the destination path'
	destination = raw_input('>')
	if destination is '' or source is '':
		print 'Aborting!'
		return
	if 's3://' not in destination and destination[len(destination) - 1] != '/':
		print 'Destination path doesnot look good! Enter again'
		return
	if '/' not in source:
		print 'Source path doesnot look good! Enter again'
		return
	f = open(path + '/out/source.txt', 'w')
	source = 'source=' + str(source)
	destination = 'destination=' + str(destination)
	f.write(source + '\n' + destination)
	print 'All done. Updated!'


def get_key_list(path):
	file_name = path + '/out/success.txt'
	success = []
	f = open(file_name, 'r')
	for line in f.readlines():
		success.append(line.strip())
	return success


def save_list(path, data, file_name):
	file_name = path + '/out/' + file_name + '.txt'
	f = open(file_name, 'w')
	for line in data:
		f.write(line)
	f.close()
