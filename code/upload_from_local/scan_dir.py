import aws_hyve
from sys import exit


def run_8():
	source, dest = aws_hyve.files.get_paths()

	if source is None:
		print 'source and/or destination paths is/are not correct. Check and update resources/PATHS file'
		exit(0)

	print 'Analyzing files! This will take time'
	aws_hyve.files.get_list(source, dest)
	aws_hyve.trimmer.trim_file_list('out/temp.txt', dest)
	success, error = aws_hyve.trimmer.check('out/trimmed.txt')
	aws_hyve.files.save_list(success, 'out/success.txt')
	if not len(error) == 0:
		print 'There were a few errors. Please check errors.txt and success.txt'
		aws_hyve.files.save_list(error, 'out/errors.txt')
		# exit(0)

	if not len(success) == 0:
		aws_hyve.common.confirm('Upload to aws S3 bucket?')
		aws_hyve.files.upload_to_aws(success, source, dest)
		print 'All clear! syncing files with s3 buckets'

	print 'All files are properly synced'
