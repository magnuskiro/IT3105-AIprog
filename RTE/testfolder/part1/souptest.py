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

# Test-data, a small subset of the RTE2_dev.preprocessed		
#file_name = "testingdata.xml"

# The xml-file to be analyzed
file_name = "RTE2_dev.preprocessed.xml"		
file = open(file_name, "r")
soup = BeautifulStoneSoup(file.read())

# Used for debugging
line_no = 666

text = []
hypothesis = []
lemmas = []
pos = []
words = []

# Creates a text_node that contains all text between <text></text> tags
# From this text_node, text between lemma-, pos-tag-, and word-tags are
# extracted
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

# Same as above, only with hypothesis instead of text	
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

# Removes tabs and newlines, and joins the list of characters
# to form a list of words
def strip_words(words):
	stripped = []
	for i in range(len(words)):
		stripped.append(words[i].split())
	for i in range(len(stripped)):
		stripped[i] = ''.join(stripped[i])
	stripped = map(lambda x : x.lower(), stripped)
	return stripped
	
# Takes in a list of pos-tags and words, and generates a list of 
# pos-tag/word pairs i.e word = hello, pos-tag = U, result = helloU	
def create_pos_lemma(pos, word):
	try:
		pw = []
		for i in range(len(word)):
			s = word[i] + pos[i]
			if s[0].isalpha() or s[0].isdigit():
				pw.append(s)
	except:
		pw.append("")
	return pw

# Removes empty characters ('') from the list of lemmas	
def remove(a):
	b = []
	for i in a:
		if len(i) > 0:
			b.append(i)
	return b

no_lemmas = []
no_pos = []
tpw = []
hpw = []
t_p_ls = []
h_p_ls = []
lemmas = []
for i in range(len(hypothesis)):
	t = text[i]
	h = hypothesis[i]
	
	t_lemmas = strip_words(t.lemmas)
	t_words = strip_words(t.words)
	t_pos = strip_words(t.pos)
	h_lemmas = strip_words(h.lemmas)
	h_words = strip_words(h.words)
	h_pos = strip_words(h.pos)	
	
	if i == line_no:
		print h_words
		print h_lemmas
	
	t_p_l = create_pos_lemma(t_pos, t_lemmas)
	h_p_l = create_pos_lemma(h_pos, h_lemmas)
	t_p_ls.append(t_p_l)
	h_p_ls.append(h_p_l)

# For debugging	
#	if i == line_no:
#		print t_p_l, h_p_l
		
	t_lemmas = map(lambda x : x.strip('.,:;-~"'), t_lemmas)
	t_words = map(lambda x : x.strip('.,:;-~"'), t_words)
	t_pos = map(lambda x : x.strip('.,:;-~"'), t_pos)
	h_lemmas = map(lambda x : x.strip('.,:;-~"'), h_lemmas)
	h_words = map(lambda x : x.strip('.,:;-~"'), h_words)
	h_pos = map(lambda x : x.strip('.,:;-~"'), h_pos)
	
	t_lemmas = remove(t_lemmas)
	h_lemmas = remove(h_lemmas)
	lemmas.append(h_lemmas)

# For debugging	
#	if i == line_no:
#		print len(h_lemmas), len(h_pos)
		
    # Counts lemmas that occur in both text and hypothesis
	x = 0
	for l in h_lemmas:
		if l in t_lemmas:
			x += 1
	no_lemmas.append(x)
	
	# Count pos-tag/word-combinations that occur in both text and hypothesis
	x = 0
	for p in h_p_l:
		if p in t_p_l:
			x += 1
	no_pos.append(x)
	
	if i == line_no:
		print h_p_l
		print t_p_l
		
		
#print len(lemmas), len(no_pos), len(pos)
lemma_match = []
pos_match = []
for i in range(len(lemmas)):
	lemma_match.append((no_lemmas[i]*1.0) / len(lemmas[i]))
	pos_match.append((no_pos[i]*1.0) / len(h_p_ls[i]))

# Writes all the lemmas to file
out = "lemma_matches2.txt"
file = open(out, 'wb')
if file:
	for i in lemma_match:
		print >> file, i
	file.close()
else:
	print "Error opening file"
	
# Writes all the pos-tags to file
out = "pos_tag_matches2.txt"
file = open(out, 'wb')
if file:
	for i in pos_match:
		print >> file, i
	file.close()
else:
	print "Error opening file"

# Call predict with step_size and wordmatches to find best threshold
lemma_name = "lemma_matches2.txt"
pos_word_name = "pos_tag_matches2.txt"
step_size = 0.001
predict.predict(step_size, lemma_name)
predict.predict(step_size, pos_word_name)



