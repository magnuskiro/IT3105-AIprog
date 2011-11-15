from BeautifulSoup import BeautifulStoneSoup
from xml.sax.handler import ContentHandler
from xml.sax import parse

#***********************************************************	
# Objects to hold the texts' and hypothesis' 
# lemmas and pos-tags				   
#***********************************************************	
class Text():
	def __init__(self):
		self.words = []
		self.lemmas = []
		self.pos = []
		
class Hypothesis():
	def __init__(self):
		self.words = []
		self.lemmas = []
		self.pos = []
		
		
file = open("testingdata.xml", "r")
soup = BeautifulStoneSoup(file.read())

text = []
hypothesis = []
lemmas = []
pos = []
words = []

index = 0
for text_node in soup.findAll("text"):
	text.append(Text())
	for node in text_node.findAll("lemma"):
		text[index].lemmas.append(''.join(node.findAll(text=True)))
	for node in text_node.findAll("pos-tag"):
		text[index].pos.append(''.join(node.findAll(text=True)))
	for node in text_node.findAll("word"):
		text[index].words.append(''.join(node.findAll(text=True)))
	index += 1
	
index = 0
for hypothesis_node in soup.findAll("hypothesis"):
	hypothesis.append(Hypothesis())
	for node in hypothesis_node.findAll("lemma"):
		hypothesis[index].lemmas.append(''.join(node.findAll(text=True)))
	for node in hypothesis_node.findAll("pos-tag"):
		hypothesis[index].pos.append(''.join(node.findAll(text=True)))
	for node in hypothesis_node.findAll("word"):
		hypothesis[index].words.append(''.join(node.findAll(text=True)))
	index += 1

print len(text), len(hypothesis)
for i in range(len(hypothesis)):
	t = text[i]
	h = hypothesis[i]
	t_l = t.lemmas
	t_p = t.pos
	t_w = t.words
	h_l = h.lemmas
	h_p = h.pos
	h_w = h.words
	t.lemmas = [x.strip(' \t\n,.') for x in t_l]
	t.pos = [x.strip(' \t\n,.') for x in t_p]
	t.words = [x.strip(' \t\n,.') for x in t_w]
	h.lemmas = [x.strip(' \t\n,.') for x in h_l]
	h.pos = [x.strip(' \t\n,.') for x in h_p]
	h.words = [x.strip(' \t\n,.') for x in h_w]

t1 = hypothesis[0]
for i in range(len(t1.words)):
	if t1.words[i] != '':
		print t1.lemmas[i], t1.pos[i], t1.words[i]



