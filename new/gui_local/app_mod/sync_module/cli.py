from __future__ import division
from subprocess import Popen, PIPE
import codecs


def get_list(path, source, dest):
	cmd = 'aws s3 sync --dryrun '
	exclude = '--exclude "." --exclude ".ini" --exclude "*.ini" --exclude ".picasaoriginals" '
	include = '--include "/menus/.jpg" --include "/photos/.jpg" '
	extra_cards = '--size-only '
	source = source + ' '
	dest = dest + ' '
	stdout = '> ' + path + '/out/temp.txt'
	cmd = cmd + exclude + include + extra_cards + source + dest + stdout
	process = Popen([cmd], shell=True, stdin=PIPE, stderr=PIPE)
	return process.communicate()


def trim_file_list(path, dest):
	file_name = path
	f = codecs.open(file_name + '/out/temp.txt', 'r', 'utf-8')
	o = open(path + '/out/trimmed.txt', 'w')
	for line in f.readlines():
		if 'Completed ' not in line:
			o.write(line[line.find(dest) + len(dest):])
	f.close()
	o.close()


def check(path):
	file_name = path + '/out/trimmed.txt'
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


def upload_to_aws(local_path, success, source, dest, console, progress):
	aws_cmd = 'aws s3 cp '
	progress_count = 0
	for key in success:
		# last character is eol
		cmd = aws_cmd + source + key + ' ' + dest + key
		console.emit(1, 'command-->' + str(cmd))
		process = Popen([cmd], shell=True, stdin=PIPE, stderr=PIPE)
		console.emit(1, str(process.communicate()))
		progress_count += 1
		if progress_count % (len(success) / 100) == 0:
			progress.emit(progress_count / (len(success) / 100))
