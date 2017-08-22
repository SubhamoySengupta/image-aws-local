import sync_files


def run():
	print 'ACT-1: Checking files in hyve-stores and hyve-rootwork'
	input_params = sync_files.input_params.get_credentials()

	f = open('out/hyve-rootwork_keys.txt', 'w')
	g = open('out/hyve-stores_keys.txt', 'w')

	conn = sync_files.aws_con.connect_S3(input_params)

	conn.connect_to_aws_bucket('hyve-rootwork')
	root_list = conn.bucket.list()
	root_list_trimmed = {}

	for item in root_list:
		if '.jpg' in item.name:
			t = item.name
			t = t[t.find('/') + 1:]
			t_1 = t[:t.find('/')]
			t = t[t.find('/') + 1:]
			t_2 = t[:t.find('/')]
			t = t[t.find('/') + 1:]
			t_3 = t[:t.find('/')]
			if t_1 not in root_list_trimmed:
				root_list_trimmed[t_1] = {}
			if t_2 in root_list_trimmed[t_1]:
				root_list_trimmed[t_1][t_2].append(t_3)
			else:
				root_list_trimmed[t_1][t_2] = []
				root_list_trimmed[t_1][t_2].append(t_3)
			f.write(item.name + '\n')

	conn.connect_to_aws_bucket('hyve-stores')
	store_list = conn.bucket.list()
	store_list_trimmed = {}

	for item in store_list:
		if '.jpg' in item.name and '/__w-' in item.name:
			t = item.name
			t_0 = t[:t.find('/')]
			t = t[t.find('/') + 1:]
			t_1 = t[:t.find('/')]
			t = t[t.find('/') + 1:]
			t_2 = t[:t.find('/')]
			t = t[t.find('/') + 1:]
			t_3 = t[:t.find('/')]
			if t_0 not in store_list_trimmed:
				store_list_trimmed[t_0] = {}
			if t_1 not in store_list_trimmed[t_0]:
				store_list_trimmed[t_0][t_1] = {}
			if t_2 in store_list_trimmed[t_0][t_1]:
				store_list_trimmed[t_0][t_1][t_2].append(t_3)
			else:
				store_list_trimmed[t_0][t_1][t_2] = []
				store_list_trimmed[t_0][t_1][t_2].append(t_3)
			g.write(item.name + '\n')

	for d in root_list_trimmed:
		for e in store_list_trimmed:
			if d == e:
				for pmr in root_list_trimmed[d]:
					for pms in store_list_trimmed[e]:
						if pms == pmr:
							for ws in store_list_trimmed[e][pms]:
								for ims in range(len(store_list_trimmed[e][pms][ws])):
									chu = ''
									if store_list_trimmed[e][pms][ws][ims] in root_list_trimmed[d][pmr]:
										chu = 's'
									if chu != 's':
										print 'Duplicate'
										print e + '/' + pms + '/' + store_list_trimmed[e][pms][ws][ims]
										duplicates = delete_this_image(e, pms, store_list_trimmed[e][pms][ws][ims], store_list)
										for keys in duplicates:
											conn.delete_duplicates(keys)


def delete_this_image(slug, pm, image_name, store_list):
	duplicates = []
	duplicate_file = open('out/duplicates.txt', 'w')
	for img in store_list:
		if slug in img and pm in img and image_name in img:
			duplicate_file.write(img)
			duplicates.append(img[:len(img) - 1])
	return duplicates
