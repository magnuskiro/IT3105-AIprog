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
		self.relations = []
		
class Hypothesis():
	def __init__(self):
		self.words = []
		self.lemmas = []
		self.pos = []
		self.relations = []
		

#***********************************************************	
# Parses the xml-file and extracts the lemmas and pos-tags		   
# found between <text></text> and creates a text object
# for each text found
#***********************************************************
class TextHandler(ContentHandler):

	passthrough = False
	in_lemma = False
	in_pos = False
	index = 0    
	
	def __init__(self, text):
		ContentHandler.__init__(self)
		self.text = text
		self.data = []
		self.lemma = []
		self.pos = []
		
	def startElement(self, name, attrs):
		if name == "text":
			self.passthrough = True
			self.text.append(Text())
		elif self.passthrough:
			if name == "lemma":
				self.in_lemma = True
			if name == "pos-tag":
				self.in_pos = True
	
	def endElement(self, name):
		if name == "text":
			self.passthrough = False
			l = ''.join(self.lemma)
			p = ''.join(self.pos)
			self.lemma = []
			self.pos = []
			self.text[self.index].lemmas.append(l)
			self.text[self.index].pos.append(p)
			self.index += 1
		if name == "lemma":
			self.in_lemma = False
		if name == "pos-tag":
			self.in_pos = False
	
	def characters(self, string):
		if self.in_lemma:
			self.lemma.append(string)
		if self.in_pos:
			self.pos.append(string)
    

#***********************************************************	
# Parses the xml-file and extracts the lemmas and pos-tags		   
# found between <hypothesis></hypothesis> and creates a 
# hypothesis object for each hypothesis found
#***********************************************************
class HypothesisHandler(ContentHandler):
	
	passthrough = False
	in_lemma = False
	in_pos = False
	index = 0
	
	def __init__(self, hypothesis):
		ContentHandler.__init__(self)
		self.hypothesis = hypothesis
		self.data = []
		self.lemma = []
		self.pos = []
		
	def startElement(self, name, attrs):
		if name == "hypothesis":
			self.passthrough = True
			self.hypothesis.append(Hypothesis())
		elif self.passthrough:
			if name == "lemma":
				self.in_lemma = True
			if name == "pos-tag":
				self.in_pos = True
	
	def endElement(self, name):
		if name == "hypothesis":
			self.passthrough = False
			l = ''.join(self.lemma)
			p = ''.join(self.pos)
			self.lemma = []
			self.pos = []
			self.hypothesis[self.index].lemmas.append(l)
			self.hypothesis[self.index].pos.append(p)
			self.index += 1
		if name == "lemma":
			self.in_lemma = False
		if name == "pos-tag":
			self.in_pos = False
	
	def characters(self, string):
		if self.in_lemma:
			self.lemma.append(string)
		if self.in_pos:
			self.pos.append(string)
			
# Uses the content handlers to extract texts and hypothesis from the xml-file				   			
text = []
hypothesis = []
parse("RTE2_dev.preprocessed.xml", TextHandler(text))
parse("RTE2_dev.preprocessed.xml", HypothesisHandler(hypothesis))

# Just to check that all text and hypothesis entries have been processed
print len(text)
print len(hypothesis)

#***********************************************************
# Used for testing
#***********************************************************
## Get the first text and hypothesis, then their lemmas and pos-tags
#t = text[0]
#h = hypothesis[0]
#t_lemmas = t.lemmas[0]
#t_pos = t.pos[0]
#h_lemmas = h.lemmas[0]
#h_pos = h.pos[0]

## Remove tabs
#t_lemmas = t_lemmas.split("\t")
#t_pos = t_pos.split("\t")
#h_lemmas = h_lemmas.split("\t")
#h_pos = h_pos.split("\t")

## Remove newlines, punctuations and duplicates TODO: Are duplicates wanted or unwanted?
#t_lemmas = map(lambda x : x.strip('"\n".,:;"'), t_lemmas)
#t_pos = map(lambda x : x.strip('"\n".,:;"'), t_pos)
#h_lemmas = map(lambda x : x.strip('"\n".,:;"'), h_lemmas)
#h_pos = map(lambda x : x.strip('"\n".,:;"'), h_pos)
#t_lemmas = set(t_lemmas)
#t_pos = set(t_pos)
#h_lemmas = set(h_lemmas)
#h_pos = set(h_pos)
#print "length of lemmas", len(h_lemmas)
#no_lemmas = 0
#no_pos = 0

#for i in t_lemmas:
#    if i in h_lemmas:
#        no_lemmas += 1
#for i in t_pos:
#    if i in h_pos:
#        no_pos += 1
#        
#print no_lemmas, no_pos


lemmas = []
pos = []
no_lemmas = []
no_pos = []
for i in range(len(text)):
    # Get the first text and hypothesis, then their lemmas and pos-tags
    t = text[i]
    h = hypothesis[i]
    t_lemmas = t.lemmas[0]
    t_pos = t.pos[0]
    h_lemmas = h.lemmas[0]
    h_pos = h.pos[0]

    # Remove tabs
    t_lemmas = t_lemmas.split("\t")
    t_pos = t_pos.split("\t")
    h_lemmas = h_lemmas.split("\t")
    h_pos = h_pos.split("\t")

    # Remove newlines, punctuations and duplicates TODO: Are duplicates wanted or unwanted?
    t_lemmas = map(lambda x : x.strip('"\n".,:;"'), t_lemmas)
    t_pos = map(lambda x : x.strip('"\n".,:;"'), t_pos)
    h_lemmas = map(lambda x : x.strip('"\n".,:;"'), h_lemmas)
    h_pos = map(lambda x : x.strip('"\n".,:;"'), h_pos)
    t_lemmas = set(t_lemmas)
    t_pos = set(t_pos)
    h_lemmas = set(h_lemmas)
    h_pos = set(h_pos)
    lemmas.append(h_lemmas)
    pos.append(h_pos)
    
    # Counts lemmas that occur in both text and hypothesis
    x = 0
    for l in t_lemmas:
    	if l in h_lemmas:
    		x += 1
    no_lemmas.append(x)

	# Count pos-tags that occur in both text and hypothesis
    x = 0
    for p in t_pos:
    	if p in h_pos:
    		x += 1
    no_pos.append(x)

# Calculate normalized values for lemma and pos-tag matching
lemma_match = []
pos_match = []
for i in range(len(lemmas)):
	lemma_match.append((no_lemmas[i]*1.0) / len(lemmas[i]))
	pos_match.append((no_pos[i]*1.0) / len(pos[i]))

# Writes all the lemmas to file
out = "lemma_matches.txt"
file = open(out, 'wb')
if file:
	for i in lemma_match:
		print >> file, i
	file.close()
else:
	print "Error opening file"

# Writes all the pos-tags to file
out = "pos-tag_matches.txt"
file = open(out, 'wb')
if file:
	for i in pos_match:
		print >> file, i
	file.close()
else:
	print "Error opening file"

# Call predict with step_size and wordmatches to find best threshold
lemma_name = "lemma_matches.txt"
pos_name = "pos-tag_matches.txt"
step_size = 0.00001
predict.predict(step_size, pos_name)
    
