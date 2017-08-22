import os


BASE_PATH = '/run/user/1000/gvfs/smb-share:server=192.168.0.51,share=hyve/hyve-rootwork/'

new_f = open('new.txt', 'r')
cur_f = open('cur.txt', 'r')
del_f = open('del.txt', 'r')
new = []
cur = []
del1 = []
for line in new_f.readlines():
	new.append(BASE_PATH + line[:-1])

for line in cur_f.readlines():
	cur.append(BASE_PATH + line[:-1])

for line in del_f.readlines():
	del1.append(BASE_PATH + line[:-1])

for i in range(len(cur)):
	try:
		os.rename(cur[i], new[i])
		print i
	except:
		print 'Coudlnot rename =====> ', cur[i]

for f_name in del1:
	try:
		os.remove(f_name)
	except:
		print 'Couldnot delete====> ', f_name
