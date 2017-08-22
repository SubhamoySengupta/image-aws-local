f = open('store.txt', 'r')
g = open('root.txt', 'r')
h = open('diff', 'w')
store = []
root = []
for line in f.readlines():
	store.append(line)

for line in g.readlines():
	root.append(line)

for s in store:
	check = False
	for r in root:
		if s == r:
			check = True

	if check is False:
		h.write(s)
		print s
