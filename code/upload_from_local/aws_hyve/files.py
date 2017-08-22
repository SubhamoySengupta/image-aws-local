from subprocess import Popen, PIPE


def get_paths():
	f = open('resources/path.txt', 'r')
	try:
		for line in f.readlines():
			if 'source = ' in line:
				source = line[line.find('=') + 1:]
			if 'destination = ' in line:
				dest = line[line.find('=') + 1:]
		return source.strip(), dest.strip()
	except:
		return None, None


def get_list(source, dest):
	cmd = 'aws s3 sync --dryrun '
	exclude = '--exclude "." --exclude ".ini" --exclude "*.ini" --exclude ".picasaoriginals" '
	include = '--include "/menus/.jpg" --include "/photos/.jpg" '
	extra_cards = '--size-only '
	source = source + ' '
	dest = dest + ' '
	stdout = '> out/temp.txt'
	cmd = cmd + exclude + include + extra_cards + source + dest + stdout
	process = Popen([cmd], shell=True, stdin=PIPE, stderr=PIPE)
	return process.communicate()


def save_list(data, file_name):
	f = open(file_name, 'w')
	for line in data:
		f.write(line)
	f.close()


def upload_to_aws(success, source, dest):
	aws_cmd = 'aws s3 cp '
	for key in success:
		# last character is eol
		cmd = aws_cmd + source + key[:len(key) - 1] + ' ' + dest + key[:len(key) - 1]
		print 'command-->', cmd
		process = Popen([cmd], shell=True, stdin=PIPE, stderr=PIPE)
		print process.communicate()
		path = '//hyve-rootwork/' + key
		cmd = 'chmod +x resources/queue_1'
		process1 = Popen([cmd], shell=True, stdin=PIPE, stderr=PIPE)
		print process1.communicate()
		cmd = 'resources/queue_1 ' + path
		process2 = Popen([cmd], shell=True, stdin=PIPE, stderr=PIPE)
		print process2.communicate()
