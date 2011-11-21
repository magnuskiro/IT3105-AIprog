#file = open("RTE2.txt")

#text = file.read()

#nodes = text.split("</node>")

## Remove last entry in nodes, not a true node
#nodes = nodes[:len(nodes)-1]

#node1 = nodes[0].split(",")

## The format of RTE2.txt means that the first lines of 
## the preprocessed data will be a part of node1, therefore
## we must remove the first lines of this node, also remove
## last element, as this is empty
#node1 = node1[5:]

#from xml.sax.handler import ContentHandler
#from xml.sax import parse

#class PageMaker(ContentHandler):
#	passthrough = False
#	def startElement(self, name, attrs):
#		if name == "node":
#			self.passthrough = True
#			print attrs["id"]
#	def endElement(self, name):
#		if name == "node":
#			self.passthrough = False
#			print "done"
#	def characters(self, chars):
#		print charst = 
#		
#parse("formatted.xml", PageMaker())


from BeautifulSoup import BeautifulStoneSoup
from xml.sax.handler import ContentHandler
from xml.sax import parse
import predict


#class Node(object):

#	def __init__(self, label):
#		self.label = label
#		self.children = list()
#		
#	def add_child(self, node, before=False):
#		if before:
#			self.children.insert(0, node)
#		else:
#			self.children.append(node)
#		return self
#		
#	def get(self, label):
#		if self.label = label: 
#			return self
#		for child in self.children:
#			if label in child:
#				return child.get(label)
#	
#	def iter(self):
#		queue = collection.deque()
#		queue.append(self)
#		while len(queue) > 0:
#			next = queue.popleft()
#			for child in next.children:
#				queue.append(child)
#			yield next
#			
#	def __contains__(self, b):
#		if isinstance(b, str) and self.label == b:
#			return 1
#		elif not isinstance(b, str) and self.label == b.label:
#			return 1
#		elif (isinstance(b, str) and self.label != b) or self.label != b.label:
#			return(sum(b in c for c in self.children)
#		raise TypeError, "Object %s is not of type str or Node" % repr(b)
#		
#	def __eq__(self, b):
#		if b is None:
#			return False
#		if not isinstance(b, Node):
#			raise TypeError, "Must compare against type Node"
#		return self.label == b.label
#		
#	def __ne__(self, b):
#		return not self.__eq__(b)
#		
#	def __repr__(self):
#		return super(Node, self).__repr__()[:-1] + " %>" % self.label
#		
#	def __str__(self):
#		s = "%d:%s" % (len(self.children), self.label)
#		s = "\n".join([s]+[str(c) for c in self.children])
#		return s
		


file_name = "longformatted.xml"
file = open(file_name)
soup = BeautifulStoneSoup(file.read())

nodes = soup.findAll("node")
node1 = nodes[1]
node1content = ''.join(node1.findAll(text = True))
node1content = node1content.split()

# To extract relation (empty relation returns empty value)
node1relation = node1.relation

# To find node id
node1id = str(node1.attrs[0][1])

# To find node parent
node1parent = str(node1.relation.attrs[0][1])

# To read entire xml-file
file = open("longformatted.xml") # not entire file, just a larger sample
soup = BeautifulStoneSoup(file.read())

# Find all nodes in all T and H
text_nodes = []
for node in soup.findAll("text"):
	text_nodes.append(node.findAll("node"))
	
hypo_nodes = []
for node in soup.findAll("hypothesis"):
	hypo_nodes.append(node.findAll("node"))
	


