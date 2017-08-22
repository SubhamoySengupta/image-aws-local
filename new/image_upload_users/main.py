import modules
import os
import urllib
from subprocess import Popen, PIPE


path = os.path.dirname(os.path.realpath(__file__))
base_url = 'https://s3-ap-southeast-1.amazonaws.com/hyve-users/'

cred = modules.credentials.get_credentials(path)

conn = modules.aws_con.connect_s3(cred)

conn.connect_to_aws_bucket(cred['in_bucket'])

user_image_list = conn.bucket.list()

# 00NNW8/N9e2B4s146nCLxkKGtxWnBjOUJ9D7cx0.jpg
# exclude
# dir/__w__/...
# dir/wxxx/....


user_image_list_trimmed = modules.trim.user_list(user_image_list)

for dir_id in user_image_list_trimmed:
	image_list = user_image_list_trimmed[dir_id]['image_list']
	for image in image_list:
		print dir_id + '/' + image
		file_name = base_url + dir_id + '/' + image
		file_blob = modules.trim.read_image(file_name, image)
		pic = modules.pic.image_resizer(image)
		pic.get_dimensions()
		w_dir = pic.DIMENSION
		new_key_name = dir_id + '/' + w_dir + '/' + image
		new_image_key = conn.bucket.new_key(new_key_name)
		if image.split('.')[1] is 'jpg' or image.split('.')[1] is 'JPG' or image.split('.')[1] is 'jpeg':
			new_image_key.set_metadata("Content-Type", 'image/jpeg')
		elif image.split('.')[1] is 'png' or image.split('.')[1] is 'PNG':
			new_image_key.set_metadata("Content-Type", 'image/png')
		new_image_key.set_contents_from_filename(image)
		new_image_key.set_acl('public-read')
		conn.bucket.delete_key(dir_id + '/' + image)
		os.remove(image)


# user_image_list = conn.bucket.list()

# f = open(path + '/out/key_list', 'w')

# for key in user_image_list:
# 	if '/__w' in key.name:
# 		f.write('//' + cred['in_bucket'] + '/' + key.name + '\n')
# f.close()

# # start iron tasks
# cmd = 'chmod +x ' + path + '/resources/queue'
# process1 = Popen([cmd], shell=True, stdin=PIPE, stderr=PIPE)
# print process1.communicate()
# cmd = path + '/resources/queue ' + path + '/out/key_list'
# process2 = Popen([cmd], shell=True, stdin=PIPE, stderr=PIPE)
# print process2.communicate()
