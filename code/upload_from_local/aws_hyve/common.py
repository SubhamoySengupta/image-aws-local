from sys import exit


def confirm(msg):
	print msg + '(Y/n)'
	feedback = raw_input('>')
	if feedback is 'Y' or feedback is 'y':
		return ''
	else:
		exit(0)
