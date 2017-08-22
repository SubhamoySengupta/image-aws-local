from __future__ import division
import sync_module
import os
path = os.path.dirname(os.path.realpath(__file__))


def dryrun(console, progress):
	console.emit(2, 'Analyzing files! This will take time')
	console.emit(1, '=====================================')
	source, dest = sync_module.paths.get_path(path)
	sync_module.cli.get_list(path, source, dest)
	sync_module.cli.trim_file_list(path, dest)
	success, error = sync_module.cli.check(path)
	sync_module.paths.save_list(path, success, 'success')
	if not len(error) == 0:
		sync_module.paths.save_list(path, error, 'error')
		console.emit(1, 'There were a few errors. Please check errors.txt and success.txt')
	if len(success) == 0:
		console.emit(1, 'Dryrun Complete. No new keys found')
	else:
		for s in success:
			console.emit(1, str(s))
		console.emit(1, '=================================================')
		console.emit(1, 'Dryrun Complete. List of new keys are stored in success.txt')


def sync(console, progress):
	# dryrun(console, progress)
	source, dest = sync_module.paths.get_path(path)
	success = sync_module.paths.get_key_list(path)
	if len(success) > 0:
		console.emit(1, 'Started copying files to S3')
		console.emit(1, '=====================================')
		sync_module.cli.upload_to_aws(path, success, source, dest, console, progress)
	else:
		console.emit(1, 'Nothing to sync :(')


def config():
	sync_module.paths.update(path)
