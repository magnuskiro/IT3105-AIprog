from BeautifulSoup import BeautifulStoneSoup
from xml.sax.handler import ContentHandler
from xml.sax import parse
import predict

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
		
file_name = "testingdata.xml"
#file_name = "RTE2_dev.preprocessed.xml"		
file = open(file_name, "r")
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

no_lemmas = []
no_pos_word = []
tpw = []
hpw = []
for i in range(len(hypothesis)):
	t = text[i]
	h = hypothesis[i]
	
	if i == 0:
		print t.lemmas[0]
		t.lemmas = str(t.lemmas)
		print t.lemmas[0].split()
	
	t.lemmas = [x.strip(' \t\n,.') for x in t.lemmas]
	t.pos = [x.strip(' \t\n,.') for x in t.pos]
	t.words = [x.strip(' \t\n,.') for x in t.words]
	h.lemmas = [x.strip(' \t\n,.') for x in h.lemmas]
	h.pos = [x.strip(' \t\n,.') for x in h.pos]
	h.words = [x.strip(' \t\n,.') for x in h.words]

	text_word_lemma = []
	for l in range(len(t.words)):
		text_word_lemma.append(t.lemmas[l])
	
	hypo_word_lemma = []
	for l in range(len(h.words)):
		hypo_word_lemma.append(h.lemmas[l])
	h.lemmas = hypo_word_lemma
	
#	text_pos_word = {}
#	x = 0
#	for l in t.words:
#		text_pos_word[l] = t.pos[x]
#		x += 1
#	tpw.append(text_pos_word)
		
#	hypo_pos_word = {}
#	x = 0
#	for l in h.words:
#		hypo_pos_word[l] = h.pos[x]
#		x += 1
#	hpw.append(hypo_pos_word)

	text_pos_word = []
	x = 0
	for l in range(len(t.words)):
		text_pos_word.append(t.words[l] + t.pos[l])
	tpw.append(text_pos_word)

	hypo_pos_word = []
	x = 0
	for l in range(len(h.words)):
		hypo_pos_word.append(h.words[l] + h.pos[l])
	hpw.append(hypo_pos_word)
		
	x = 0
	for l in hypo_word_lemma:
		if l in text_word_lemma:
			x += 1
	no_lemmas.append(x)
	
	x = 0
	for i in hypo_pos_word:
		if i in text_pos_word:
			x += 1
	no_pos_word.append(x)

lemma_match = []
for i in range(len(hypothesis)):
	h = hypothesis[i]
	lemma_match.append((no_lemmas[i] * 1.0) / len(h.lemmas))
#print text_pos_word

pos_word_match = []
for i in range(len(hpw)):
	h = hpw[i]
	pos_word_match.append((no_pos_word[i] * 1.0) / len(h))
		


## Writes all the lemmas to file
#out = "lemma_matches2.txt"
#file = open(out, 'wb')
#if file:
#	for i in lemma_match:
#		print >> file, i
#	file.close()
#else:
#	print "Error opening file"
#	
## Writes all the pos-tags to file
#out = "pos_tag_matches2.txt"
#file = open(out, 'wb')
#if file:
#	for i in pos_word_match:
#		print >> file, i
#	file.close()
#else:
#	print "Error opening file"

## Call predict with step_size and wordmatches to find best threshold
#lemma_name = "lemma_matches2.txt"
#pos_word_name = "pos_tag_matches2.txt"
#step_size = 0.001
#predict.predict(step_size, lemma_name)
#predict.predict(step_size, pos_word_name)



