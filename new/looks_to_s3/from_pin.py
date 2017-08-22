import modules
import os
import urllib
from subprocess import Popen, PIPE

path = os.path.dirname(os.path.realpath(__file__))
base_url = 'https://s3-ap-southeast-1.amazonaws.com/hyve-users/'

local_disk_path = '/run/user/1000/gvfs/smb-share:server=192.168.0.51,share=hyve/looks/hair-style-men/'

local_look_list = modules.trim.get_pin_list(path)

for image_file in local_look_list:
	image_link = image_file.split(',')[2]
	image_type = image_link[image_link.rfind('.') + 1:]
	pin = image_file.split(',')[0] + '.' + image_type
	f = open(local_disk_path + pin, 'wb')
	f.write(urllib.urlopen(image_link).read())
	f.close()
	print pin

# cred = modules.credentials.get_credentials(path)

# conn = modules.aws_con.connect_s3(cred)

# conn.connect_to_aws_bucket(cred['in_bucket'])


# for image_file in local_look_list:
# 	image_link = image_file.split(',')[2]
# 	image_type = image_link[image_link.rfind('.') + 1:]
# 	pin = image_file.split(',')[0] + '.' + image_type
# 	f = open(pin, 'wb')
# 	f.write(urllib.urlopen(image_link).read())
# 	f.close()
# 	image = modules.pic.image_resizer(pin)
# 	image.get_dimensions()
# 	w_path = image.DIMENSION
# 	image_name = pin
# 	new_key_name = '4NORL1/' + w_path + '/' + image_name
# 	new_image_key = conn.bucket.new_key(new_key_name)

# 	if image_name.split('.')[1] is 'jpg' or image_name.split('.')[1] is 'JPG' or image_name.split('.')[1] is 'jpeg':
# 		new_image_key.set_metadata("Content-Type", 'image/jpeg')
# 	elif image_name.split('.')[1] is 'png' or image_name.split('.')[1] is 'PNG':
# 		new_image_key.set_metadata("Content-Type", 'image/png')

# 	new_image_key.set_contents_from_filename(pin)
# 	new_image_key.set_acl('public-read')

# 	os.remove(pin)

# 	cmd = 'chmod +x ' + path + '/resources/queue_1'

# 	process1 = Popen([cmd], shell=True, stdin=PIPE, stderr=PIPE)
# 	print process1.communicate()
# 	cmd = path + '/resources/queue_1 ' + '//' + cred['in_bucket'] + '/' + new_key_name
# 	process2 = Popen([cmd], shell=True, stdin=PIPE, stderr=PIPE)
# 	print process2.communicate()
# 	print pin
