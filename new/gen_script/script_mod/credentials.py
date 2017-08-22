

def get_credentials(path):
	f = open(path + '/out/credentials.txt', 'r')
	response = dict(aws_access_key_id=None, aws_secret_access_key=None, region=None, in_bucket=None, out_bucket=None)
	for line in f.readlines():
		strings = line.split('=')
		if len(strings) == 2:
			response[strings[0].strip()] = strings[1].strip()
	return response


def update_cred(path):
	cred = dict(aws_access_key_id=None, aws_secret_access_key=None, region=None, in_bucket=None, out_bucket=None)
	cred['aws_access_key_id'] = raw_input('aws_access_key_id >')
	cred['aws_secret_access_key'] = raw_input('aws_secret_access_key >')
	cred['region'] = raw_input('region >')
	cred['in_bucket'] = raw_input('in_bucket >')
	cred['out_bucket'] = raw_input('out_bucket >')

	f = open(path + '/out/credentials.txt', 'w')
	f.write('[Credentials]\n')
	for cred, value in cred.iteritems():
		f.write(cred + ' = ' + value + '\n')
	print 'All Done! Updated**'
