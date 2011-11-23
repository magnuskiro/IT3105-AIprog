from tree_edit_dist import *

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
			
def find_distance(pair, costs=unit_costs):
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
		
	
	return distance(T_root, H_root, costs)
		
		
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
 
# Calculate the cost of inserting the whole hypothesis tree        
def insert_tree_cost(pair):
	no_nodes = 0
	for sentence in pair[1]:
		no_nodes += len(sentence.nodes)
	return no_nodes
        
        		
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
	
def run(data_set):
	taskB = open("result_part2b.txt", "wb")
	if taskB:
		for pair in data_set:
			d = find_distance(pair, unit_costs_mod)
			insert_cost = insert_tree_cost(pair)
			d = ((d*1.0) / insert_cost)
			print >> taskB, d
		taskB.close()
		print "Results from part IIb saved as 'result_part2b.txt'
	else:
		print "Error opening file"
