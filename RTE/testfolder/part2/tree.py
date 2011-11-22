from BeautifulSoup import BeautifulStoneSoup

file_name = "longformatted.xml"
file = open(file_name)
soup = BeautifulStoneSoup(file.read())

n = soup.findAll("node")
nodes = []
try:
	for i in n:
		temp = []
		temp.append(str(i.attrs[0][1]))
		if i.relation == None:
			temp.append("")
			nodes.append(temp)
			continue
		else:
			temp.append(str(i.relation.attrs[0][1]))
			nodes.append(temp)
except:
	print i
	
print nodes
d = {}

def recur_tree(value, d, key):
	if len(value) > 0:
		for i in value:
			if i in d:
				recur_tree(d[i], d, i)
		else:
			print key
	else:
		print key

for i in nodes:
	if not i[0] in d:
		d[i[0]] = [0]
	if not i[1] in d:
		d[i[1]] = []
		d[i[1]].append(i[0])
	elif i[1] in d:
		d[i[1]].append(i[0])
print d

for key, value in d.items():
	if key == "":
		recur_tree(value, d, key)


	
