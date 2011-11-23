from BeautifulSoup import BeautifulStoneSoup
import tree_edit_dist

file_name = "short2.xml"
file = open(file_name)
soup = BeautifulStoneSoup(file.read())


def make_nodes(sentence):
	nodes = []
	for node in sentence:
		temp = []
		parent = None
		isWord = False		
		temp_id = str(node.attrs[0][1])
		if temp_id[0] == "E":
			if node.lemma:
				id = node.lemma.contents
				id = map(lambda x : x.strip("\n\t"), id)
				id = str(temp_id+"-"+(''.join(id)))
			else:
				id = temp_id
		if node.relation == None:
			parent = "Root"
			temp.append(temp_id)
			temp.append(id)
			temp.append(parent)
			nodes.append(temp)
		else:
			parent = str(node.relation.attrs[0][1])
			id = node.lemma.contents + ["-"] + node.relation.contents
			id = map(lambda x : x.strip("\n\t"), id)
			id = ''.join(id).lower()
			temp.append(temp_id)
			temp.append(str(id))
			temp.append(parent)
			nodes.append(temp)
	return nodes
			
def process_node(sentence):
	temp_ids = []
	ids = []
	for n in sentence:
		temp_ids.append(n[0])
		ids.append(n[1])
		
	for n in sentence:
	#	print node
		id = n[1]
		parent = n[2]
		if parent == "Root":
			n[0] = id
			n[1] = parent
			n.pop()
			continue
		parent = ids[temp_ids.index(parent)]
		n[0] = id
		n[1] = parent
		n.pop()

	return sentence
	
def make_tree(sentence):
#	# Postorder traversal of tree
#	def recur_tree(value, d, key, a):
#		if len(value) > 0:
#			for i in value:
#				if i in d:
#					recur_tree(d[i], d, i, a)
#			else:
#				a.append(key)
#		else:
#			a.append(key)
#		return a

	d = {}
	for i in sentence:
		if not i[0] in d:
			d[i[0]] = []
		if not i[1] in d:
			d[i[1]] = []
			d[i[1]].append(i[0])
		elif i[1] in d:
			d[i[1]].append(i[0])
		
#	gg = recur_tree(d["Root"], d, "Root", [])
	return d
	



text = []
for node in soup.findAll("text"):
	text.append(node.findAll("node"))
	
hypo = []
for node in soup.findAll("hypothesis"):
	hypo.append(node.findAll("node"))
	
sentence = soup.findAll("node")
text = make_nodes(text[0])
hypo = make_nodes(hypo[0])

text = process_node(text)
hypo = process_node(hypo)

text_tree = make_tree(text)
hypo_tree = make_tree(hypo)

print hypo_tree

res = tree_edit_dist.distance(text_tree, hypo_tree)
print "distance =", res

##t1 = {"c":["b"],"d":["a","c"],"f":["d","e"], "b":[], "e":[], "a":[]} 
##t2 = {"c":["d"],"d":["a","b"],"f":["c","e"], "b":[], "e":[], "a":[]}
##test_tree1 = recur_tree(t1["f"], t1, "f", [])
##test_tree2 = recur_tree(t2["f"], t2, "f", [])
#gg = recur_tree(d["Root"], d, "Root", [])
#print gg
#print test_tree1
#print test_tree2

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


	
