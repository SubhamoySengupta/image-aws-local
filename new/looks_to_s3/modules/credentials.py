

def get_credentials(path):
	f = open(path + '/out/credentials.txt', 'r')
	response = dict(aws_access_key_id=None, aws_secret_access_key=None, region=None, in_bucket=None)
	for line in f.readlines():
		strings = line.split('=')
		if len(strings) == 2:
			response[strings[0].strip()] = strings[1].strip()
	return response
