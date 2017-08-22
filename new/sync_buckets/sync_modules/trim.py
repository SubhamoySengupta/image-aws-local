from datetime import datetime as DT


def trim_root_list(path, root_list):
	f = open(path + '/out/hyve-rootwork_keys.txt', 'w')
	root_list_trimmed = []
	# stores/slug/photos/1.jpg
	for item in root_list:
		if '.jpg' in item.name or '.png' in item.name:
			raw_dt = item.last_modified
			raw_dt = raw_dt.replace('T', ' ')
			raw_dt = raw_dt.replace('Z', '')
			raw_dt = raw_dt[:raw_dt.find('.')]
			raw_dt = DT.strptime(raw_dt, '%Y-%m-%d %H:%M:%S')

			key = item.name
			key = key[key.find('/') + 1:]
			image = dict(image_name=key, last_modified=raw_dt, key=item)
			root_list_trimmed.append(image)
			f.write(item.name + '\n')
	return root_list_trimmed


def trim_store_list(path, store_list):
	g = open(path + '/out/hyve-stores_keys.txt', 'w')
	store_list_trimmed = []
	# slug/photos/__w-100-200-400__/1.jpg
	for item in store_list:
		if ('.jpg' in item.name and '/__w-' in item.name) or ('.png' in item.name and '/__w-' in item.name):
			raw_dt = item.last_modified
			raw_dt = raw_dt.replace('T', ' ')
			raw_dt = raw_dt.replace('Z', '')
			raw_dt = raw_dt[:raw_dt.find('.')]
			raw_dt = DT.strptime(raw_dt, '%Y-%m-%d %H:%M:%S')

			key = item.name
			l = key[:key.find('/__w-')]
			r = key[key.rfind('/') + 1:]
			m = key[key.find('/__w-') + 5:]
			m = m[:m.rfind('__/')]
			m = m.split('-')
			key = l + '/' + r
			image = dict(image_name=key, last_modified=raw_dt, key=item, widths=m)
			store_list_trimmed.append(image)
			g.write(item.name + '\n')
		if ('.jpg' in item.name and '/__w__' in item.name) or ('.png' in item.name and '/__w__' in item.name):
			raw_dt = item.last_modified
			raw_dt = raw_dt.replace('T', ' ')
			raw_dt = raw_dt.replace('Z', '')
			raw_dt = raw_dt[:raw_dt.find('.')]
			raw_dt = DT.strptime(raw_dt, '%Y-%m-%d %H:%M:%S')

			key = item.name
			l = key[:key.find('/__w__')]
			r = key[key.rfind('/') + 1:]
			m = []
			key = l + '/' + r
			image = dict(image_name=key, last_modified=raw_dt, key=item, widths=m)
			store_list_trimmed.append(image)
			g.write(item.name + '\n')
	return store_list_trimmed


# root_list --> slug/photos/1.jpg
# store_list --> slug/photos/__w-100-200-400__/1.jpg
def compare_store(path, root_list_trimmed, store_list_trimmed):
	dup = []
	for item_s in store_list_trimmed:
		check = False
		for item_r in root_list_trimmed:
			if item_s['image_name'] == item_r['image_name']:
				check = True
		if check is False:
			key = str(item_s['image_name'])
			m = item_s['widths']
			width = str('-'.join(m))
			width = '__w-' + width + '__/'
			l = str(key[:key.rfind('/') + 1])
			r = str(key[key.rfind('/') + 1:])
			dup.append(str(l + width + r))
			for wi in m:
				im_link = l + 'w' + wi + '/' + r
				dup.append(str(im_link))
	return dup


def save_duplicates(path, dup):
	f = open(path + '/out/duplicates_stores.txt', 'w')
	for key in dup:
		f.write(str(key) + '\n')


def read_duplicates(path):
	f = open(path + '/out/duplicates_stores.txt', 'r')
	dup = []
	for line in f.readlines():
		dup.append(line)
	return dup


def compare_rootwork(root_list, store_list):
	new = []
	modified = []
	for item_r in root_list:
		check = False
		for item_s in store_list:
			if item_r['image_name'] == item_s['image_name']:
				check = True
				# Check if modified
				if item_r['last_modified'] > item_s['last_modified']:
					# file was modified
					modified.append(item_r)
		if check is False:
			new.append(item_r)
	return new, modified


def save_new_modified(path, new, modified):
	n = open(path + '/out/new.txt', 'w')
	m = open(path + '/out/modified.txt', 'w')
	for item in new:
		n.write(item['image_name'] + '\n')
	for item in modified:
		m.write(item['image_name'] + '\n')


def read_new_modified(path):
	n = open(path + '/out/new.txt', 'r')
	m = open(path + '/out/modified.txt', 'r')
	new = []
	modified = []
	for item in n.readlines():
		new.append(item)
	for item in m.readlines():
		modified.append(item)
	return new, modified
