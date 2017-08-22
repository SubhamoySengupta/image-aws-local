

def read_new_list(path):
	f = open(path + '/out/new.txt', 'r')
	r = []
	for line in f.readlines():
		r.append(line.strip())
	return r


def trim_store_list(store_list):
	r = []
	for item in store_list:
		if '__w-' in item.name:
			r.append(item.name)
	store_dict = {}
	# 1091-sparkle-spa/menus/__w-100-300__/1.jpg
	for item in r:
		slug = item[:item.find('/')]
		item = item[item.find('/') + 1:]
		p_m = item[:item.find('/')]
		item = item[item.find('/') + 1:]
		width = item[:item.find('/')]
		item = item[item.find('/') + 1:]
		img_name = item
		if slug not in store_dict:
			store_dict[slug] = {}
		if p_m not in store_dict[slug]:
			store_dict[slug][p_m] = {}
		if width not in store_dict[slug][p_m]:
			store_dict[slug][p_m][width] = []
		store_dict[slug][p_m][width].append(img_name)
	return store_dict


def save_script(path, script):
	f = open(path + '/out/script.sql', 'w')
	f.write(script)


def get_script(path, script):
	f = open(path + '/out/script.sql', 'r')
	return str(f.readlines())


def generate_sql(key_dict):
			sql_0 = 'UPDATE store'
			sql_p = ''
			sql_m = ''
			for slug in key_dict:
				if 'photos' in key_dict[slug]:
					images = {}
					image_urls = ''
					for w in key_dict[slug]['photos']:
						for image in key_dict[slug]['photos'][w]:
							if '.png' not in image:
								link = 'http://hyve-stores.s3.amazonaws.com/'
								link += slug + '/photos/' + w + '/' + image
								images[int(image.split('.')[0])] = link
					for string in sorted(images.items()):
						a, b = string
						image_urls += b + ','
					image_urls = image_urls[:len(image_urls) - 1]
					sql_p += sql_0 + " SET image_urls = \'" + image_urls + "' WHERE slug = '" + slug + "' "
					# sql_p += "AND image_urls is not NULL;\n"
					sql_p += ";\n"
				if 'menus' in key_dict[slug]:
					menus = {}
					menu_urls = ''
					for w in key_dict[slug]['menus']:
						for menu in key_dict[slug]['menus'][w]:
							if '.png' not in menu:
								link = 'http://hyve-stores.s3.amazonaws.com/'
								link += slug + '/menus/' + w + '/' + menu
								menus[int(menu.split('.')[0])] = link
					for string in sorted(menus.items()):
						a, b = string
						menu_urls += b + ','
					menu_urls = menu_urls[:len(menu_urls) - 1]
					sql_m += sql_0 + " SET menu_urls = \'" + menu_urls + "' WHERE slug = '" + slug + "' "
					# sql_m += "AND menu_urls is not NULL;\n"
					sql_m += ";\n"
			return sql_p + '\n\n' + sql_m


def generate_sql_null_removed(key_dict):
			sql_0 = 'UPDATE store'
			sql_p = ''
			sql_m = ''
			for slug in key_dict:
				if 'photos' in key_dict[slug]:
					images = {}
					image_urls = ''
					for w in key_dict[slug]['photos']:
						for image in key_dict[slug]['photos'][w]:
							if '.png' not in image:
								link = 'http://hyve-stores.s3.amazonaws.com/'
								link += slug + '/photos/' + w + '/' + image
								images[int(image.split('.')[0])] = link
					for string in sorted(images.items()):
						a, b = string
						image_urls += b + ','
					image_urls = image_urls[:len(image_urls) - 1]
					sql_p += sql_0 + " SET image_urls = \'" + image_urls + "' WHERE slug = '" + slug + "' "
					sql_p += ";\n"
				if 'menus' in key_dict[slug]:
					menus = {}
					menu_urls = ''
					for w in key_dict[slug]['menus']:
						for menu in key_dict[slug]['menus'][w]:
							if '.png' not in menu:
								link = 'http://hyve-stores.s3.amazonaws.com/'
								link += slug + '/menus/' + w + '/' + menu
								menus[int(menu.split('.')[0])] = link
					for string in sorted(menus.items()):
						a, b = string
						menu_urls += b + ','
					menu_urls = menu_urls[:len(menu_urls) - 1]
					sql_m += sql_0 + " SET menu_urls = \'" + menu_urls + "' WHERE slug = '" + slug + "' "
					sql_m += ";\n"
			return sql_p


def generate_sql_new_tb(key_dict):
			sql_0 = 'INSERT INTO hs_store_image (store_id, url, priority, type) VALUES '
			sql_sid = 'SELECT id FROM hs_store WHERE slug='
			sql_p = ''
			sql_m = ''

			sql_del = 'DELETE FROM hs_store_image WHERE store_id='
			sql_d = ''
			for slug in key_dict:
				if 'photos' in key_dict[slug]:
					sql_d += sql_del + "(" + sql_sid + "'" + slug + "') AND type=0;\n"
					for w in key_dict[slug]['photos']:
						image_index_priority = 0
						for image in key_dict[slug]['photos'][w]:
							if '.png' not in image:
								link = 'http://hyve-stores.s3.amazonaws.com/'
								link += slug + '/photos/' + w + '/' + image
								sql_p += sql_0 + "((" + sql_sid + "'" + slug + "'), '" + link + "', " + str(image_index_priority)
								sql_p += ", 0);\n"
								image_index_priority += 1
				if 'menus' in key_dict[slug]:
					sql_d += sql_del + "(" + sql_sid + "'" + slug + "') AND type=1;\n"
					for w in key_dict[slug]['menus']:
						image_index_priority = 0
						for menu in key_dict[slug]['menus'][w]:
							if '.png' not in menu:
								link = 'http://hyve-stores.s3.amazonaws.com/'
								link += slug + '/menus/' + w + '/' + menu
								sql_m += sql_0 + "((" + sql_sid + "'" + slug + "'), '" + link + "', " + str(image_index_priority)
								sql_m += ", 1);\n"
								image_index_priority += 1
			return sql_d + '\n\n' + sql_p + '\n\n' + sql_m
