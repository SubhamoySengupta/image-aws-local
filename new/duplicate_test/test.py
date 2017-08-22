'''
Prints duplicate keys in store __w__ directories
Check images are in order ie : 1.jpg, 2.jpg, 3.jpg, ......,
'''
import boto
import boto.s3.connection
from collections import Counter


connection = boto.s3.connect_to_region('ap-southeast-1',
					aws_access_key_id='AKIAI7CQBHPL42IO5NVA',
					aws_secret_access_key='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',
					is_secure=True,
					calling_format=boto.s3.connection.OrdinaryCallingFormat()
					)

bucket = connection.get_bucket('hyve-stores')

store_list = bucket.list()

store_dict = {}
# 379-chisel-spa-salon/photos/__w-200-400-600-800-1000-1200-1400__/99.jpg

for key in store_list:
	key_name = key.name
	if '/__w-' in key_name or '/__w__' in key_name:
		slug = key_name[:key_name.find('/')]
		pm = key_name[key_name.find('/') + 1:]
		w = pm[pm.find('/') + 1:]

		img = w[w.find('/') + 1:]
		pm = pm[:pm.find('/')]
		w = w[:w.find('/')]
		if slug not in store_dict:
			store_dict[slug] = {}
		if pm not in store_dict[slug]:
			store_dict[slug][pm] = {}
		if w not in store_dict[slug][pm]:
			store_dict[slug][pm][w] = []

		store_dict[slug][pm][w].append(img)

for slug in store_dict:
	for pm in store_dict[slug]:
		img_list = []
		for w in store_dict[slug][pm]:
			for img in store_dict[slug][pm][w]:
				img_list.append(img)

		duplicate = [img for img, dup in Counter(img_list).items() if dup > 1]
		if len(duplicate) > 0:
			key = slug + '/' + pm + '/' + '/' + w
			print key, duplicate

		if '99.jpg' in img_list:
			img_list.remove('99.jpg')
		if '0.png' in img_list:
			img_list.remove('0.png')
		no_of_images = len(img_list)

		for i in range(no_of_images):
			img_name_jpg = str(i + 1) + '.jpg'
			img_name_png = str(i + 1) + '.png'
			if img_name_jpg not in img_list and img_name_png not in img_list:
				print slug + '/' + pm + '/' + '/' + w + str(i)
