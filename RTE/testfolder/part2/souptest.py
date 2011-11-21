from BeautifulSoup import BeautifulStoneSoup
from xml.sax.handler import ContentHandler
from xml.sax import parse
import predict

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
	


