import sync_modules
import os
import sys
from subprocess import Popen, PIPE


path = os.path.dirname(os.path.realpath(__file__))


def task(arg):
	if len(arg) > 1:
		options = dict(dryrun=dryrun, sync=sync, help=help, configure=config)
		options[arg[1]]()
	else:
		print '****No arguements given. For help, type --> sync_remote.py help'


def dryrun():
	cred = sync_modules.credentials.get_credentials(path)
	conn = sync_modules.aws_con.connect_s3(cred)

	conn.connect_to_aws_bucket(cred['in_bucket'])
	root_list = conn.bucket.list()
	root_list_trimmed = sync_modules.trim.trim_root_list(path, root_list)

	conn.connect_to_aws_bucket(cred['out_bucket'])
	store_list = conn.bucket.list()
	store_list_trimmed = sync_modules.trim.trim_store_list(path, store_list)

	dup = sync_modules.trim.compare_store(path, root_list_trimmed, store_list_trimmed)
	sync_modules.trim.save_duplicates(path, dup)

	new, modified = sync_modules.trim.compare_rootwork(root_list_trimmed, store_list_trimmed)
	sync_modules.save_new_modified(path, new, modified)
	print 'Dryrun Complete!!!!!'
	print 'Found\n---------------------------------'
	print str(len(new)) + ' new files, and\n'
	print str(len(modified)) + ' modified files'
	print '\n---------------------------------\n'
	print str(len(dup)) + ' files needs to be deleted from hyve-store'


def sync():
	# dryrun()
	copy()


def copy():
	new, modified = sync_modules.trim.read_new_modified(path)
	new.extend(modified)
	print 'Copying files!'
	for key in new:
		s3_path = '//hyve-rootwork/stores/' + key
		cmd = 'chmod +x ' + path + '/resources/queue_1'
		process1 = Popen([cmd], shell=True, stdin=PIPE, stderr=PIPE)
		print process1.communicate()
		cmd = path + '/resources/queue_1 ' + s3_path
		process2 = Popen([cmd], shell=True, stdin=PIPE, stderr=PIPE)
		print process2.communicate()

	dup = sync_modules.trim.read_duplicates(path)
	cred = sync_modules.credentials.get_credentials(path)
	conn = sync_modules.aws_con.connect_s3(cred)
	conn.connect_to_aws_bucket(cred['out_bucket'])
	for key in dup:
		print key[:-1]
		try:
			conn.delete_duplicates(key[:-1])
		except:
			print 'Couldnot delete -> ', key[:-1]


def configure():
	sync_modules.credentials.update_cred(path)


def help():
	print '''\n\t\t\tOptions
=========================================================

dryrun : returns list of new keys in hyve-rootwork

sync : creates list of new keys and copies them to s3 bucket hyve-store

help : displays these options :)
'''


def config():
	print 'config'


if __name__ == '__main__':
	task(sys.argv)
