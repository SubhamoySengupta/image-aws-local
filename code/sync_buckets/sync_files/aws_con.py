import boto
import boto.s3.connection


class connect_S3:

	def __init__(self, credentials):
		try:
			self.connection = boto.s3.connect_to_region(
					credentials['region'],
					aws_access_key_id=credentials['aws_access_key_id'],
					aws_secret_access_key=credentials['aws_secret_access_key'],
					is_secure=True,
					calling_format=boto.s3.connection.OrdinaryCallingFormat()
				)
			print 'Connection to AWS S3 is successful'
		except:
			print 'Could not connect to AWS'

	def connect_to_aws_bucket(self, bucket_name):
		try:
			self.bucket = self.connection.get_bucket(bucket_name)
			print 'Connected to bucket', bucket_name
		except:
			print 'Couldnot connect to bucket', bucket_name

	def delete_duplicates(self, key):
		self.bucket.delete_key(key)
