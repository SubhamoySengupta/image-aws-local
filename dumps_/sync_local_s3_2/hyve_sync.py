import sys
import sync_module
import os

path = os.path.dirname(os.path.realpath(__file__))


def task(arg):
	if len(arg) > 1:
		options = dict(dryrun=dryrun, sync=sync, help=help, configure=config)
		options[arg[1]]()
	else:
		print '****No arguements given. For help, type --> hyve_sync.py help'


def dryrun():
	print 'Analyzing files! This will take time'
	source, dest = sync_module.paths.get_path(path)
	sync_module.cli.get_list(path, source, dest)
	sync_module.cli.trim_file_list(path, dest)
	success, error = sync_module.cli.check(path)
	sync_module.paths.save_list(path, success, 'success')
	if not len(error) == 0:
		sync_module.paths.save_list(path, error, 'error')
		print 'There were a few errors. Please check errors.txt and success.txt'
	if len(success) == 0:
		print 'Dryrun Complete. No new keys found'
	else:
		print 'Dryrun Complete. List of new keys are stored in success.txt'


def sync():
	dryrun()
	print 'Started copying files to S3'
	source, dest = sync_module.paths.get_path(path)
	sync_module.cli.upload_to_aws(path, sync_module.paths.get_key_list(path), source, dest)
	# sync_module.cli.sync_delete(path, source, dest)


def help():
	print '''\n\t\t\tOptions
=========================================================

dryrun : returns list of new keys and invalid keys

copy : copies new keys to s3 bucket

sync : creates list of new keys and copies them to s3 bucket

help : displays these options :)
'''


def config():
	sync_module.paths.update(path)


if __name__ == "__main__":
	task(sys.argv)
else:
	print 'path'
	print sync_module.paths.get_path()
