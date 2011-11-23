from BeautifulSoup import BeautifulStoneSoup
from part2adist import *

# Object representing a sentence, containing the sentence number, and a list 
# of the nodes it consists of
class Sentence(object):
	def __init__(self, sentence):
		self.serial = str(sentence.attrs[0][1])
		self.nodes = [SentenceNode(n) for n in sentence.findAll("node")]

# Represents a node in the sentence
# If a node has no relation, it is a root node
class SentenceNode(object):
	def __init__(self, node):
		self.id = str(node.attrs[0][1])
		self.parent = None
		self.word = False
		if node.relation != None:
			self.parent = str(node.relation.attrs[0][1])
		if self.id[0] == "E": 	# "artificial" node, not a word
			self.lemma = node.lemma
			if self.lemma:
				self.lemma = map(lambda x : x.strip("\n\t"), self.lemma.contents)
				self.lemma = (str(self.lemma)).lower()
		else:
			self.word = True
			self.lemma = map(lambda x : x.strip("\n\t"), node.lemma.contents)
			self.lemma = (str(self.lemma)).lower()
			self.pos_tag = map(lambda x : x.strip("\n\t"), node.find("pos-tag").contents)
			self.pos_tag = (str(self.pos_tag)).lower()
			self.relation = node.relation
			if self.relation:
				self.relation = map(lambda x : x.strip("\n\t"), self.relation.contents)
				self.relation = (str(self.relation)).lower()
			
				
def prepare_data(file_name):

	file = open(file_name)
	soup = BeautifulStoneSoup(file.read())
	text_collection = []
	for node in soup.findAll("text"):
		temp = []
		for sentence in node.findAll("sentence"):
			temp.append(Sentence(sentence))
		text_collection.append(temp)
	
	hypo_collection = []
	for node in soup.findAll("hypothesis"):
		temp = []
		for sentence in node.findAll("sentence"):
			temp.append(Sentence(sentence))
		hypo_collection.append(temp)
	
#		print len(text_collection[0]), len(hypo_collection[0])
	
	data_set = []
	for i in range(len(text_collection)):
		H_T_pair = [text_collection[i], hypo_collection[i]]
		data_set.append(H_T_pair)
		
	return data_set
			
def find_distance(pair):
	T_trees = []
	H_trees = []
	
	# pair[0] is text, pair[1] is hypothesis
	for sentence in pair[0]:
		T_trees+=(make_tree(sentence))
	for sentence in pair[1]:
		H_trees+=(make_tree(sentence))
		
	T_root = Node("top")
	H_root = Node("top")
	
	#print "T_trees :", T_trees
	for tree in T_trees:
		T_root.append(tree)
	for tree in H_trees:
		H_root.append(tree,)
		
	
	return distance(T_root, H_root)
		
		
def unit_costs_mod(node1, node2):
    """
    Defines unit cost for edit operation on pair of nodes,
    i.e. cost of insertion, deletion, substitution are all 1
    """
    # insertion cost
    if node1 is None:
        return 1
    
    # deletion cost
    if node2 is None:
        return 0
    # substitution cost
    if node1.label != node2.label:
        return 1
    else:
        return 0
        
        		
def make_tree(sentence):
	tree = {}
	root = []
	tree["root"] = Node("root")
	for node in sentence.nodes:
		if node.word:
			tree[node.id] = Node(node.lemma)
		else:
			tree[node.id] = Node(node.id)
	
	for node in sentence.nodes:
		if node.parent:
			tree[node.parent].append(tree[node.id])
		else:
			node.parent = "root"
	
	for node in sentence.nodes:
		if node.parent == "root":
			tree[node.parent].append(tree[node.id])
			
	root = tree["root"]
	return root
	

file_name = "formattedRTEdata.xml"
#file_name = "formattederror.xml"
data_set = prepare_data(file_name)
data2 = data_set[:]
print len(data_set)
taskA = open("Part IIa", "wb")
if taskA:
	for pair in data_set:
		d = find_distance(pair)
		print >> taskA, d
		print d
	taskA.close()
else:
	print "Error opening file"
	

