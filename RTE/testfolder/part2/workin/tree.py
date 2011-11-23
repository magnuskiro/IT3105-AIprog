from BeautifulSoup import BeautifulStoneSoup

file_name = "longformatted.xml"
file = open(file_name)
soup = BeautifulStoneSoup(file.read())

class Node(object):

	def __init__(self, label):
		self.label = label
		self.children = list()
		
	def addkid(self, node):
		self.children.append(node)
		return self

n = soup.findAll("node")
nodes = []
try:
	for i in n:
		temp = []
		temp.append(str(i.attrs[0][1]))
		if i.relation == None:
			temp.append("Root")
			nodes.append(temp)
			continue
		else:
			temp.append(str(i.relation.attrs[0][1]))
			nodes.append(temp)
except:
	print i
	
#print nodes
d = {}

# Postorder traversal of tree
def recur_tree(value, d, key, a):
	if len(value) > 0:
		for i in value:
			if i in d:
				recur_tree(d[i], d, i, a)
		else:
			a.append(key)
	else:
		a.append(key)
	return a

for i in nodes:
	if not i[0] in d:
		d[i[0]] = []
	if not i[1] in d:
		d[i[1]] = []
		d[i[1]].append(i[0])
	elif i[1] in d:
		d[i[1]].append(i[0])
#print d

t1 = {"c":["b"],"d":["a","c"],"f":["d","e"], "b":[], "e":[], "a":[]} 
t2 = {"c":["d"],"d":["a","b"],"f":["c","e"], "b":[], "e":[], "a":[]}
test_tree1 = recur_tree(t1["f"], t1, "f", [])
test_tree2 = recur_tree(t2["f"], t2, "f", [])
gg = recur_tree(d["Root"], d, "Root", [])
print gg
print test_tree1
print test_tree2

#print gg
#for i in gg:
#	print i[0],
#	for j in i[1]:
#		print j,

#finaltree = {}
#for i in gg:
#	if i[0] not in finaltree:
#		finaltree[i[0]] = []
#		for j in i[1]:
#			finaltree[i[0]].append(j)
#	else:
#		for j in i[1]:
#			finaltree[i[0]].append(j)
#	
#print finaltree


	
