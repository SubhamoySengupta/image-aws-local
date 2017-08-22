def get_credentials():
	cred_file = open('resources/credentials.txt', 'r')
	response = {}
	try:
		for line in cred_file.readlines():
			strings = line.split('=')
			if len(strings) == 2:
				response[strings[0].strip()] = strings[1].strip()

		if len(response) == 0:
			return False
		else:
			return response
	except:
		return None
