from xml.sax.handler import ContentHandler
from xml.sax import parse
import predict


class Hypothesis():
	
	def __init__(self):
		self.words = []
		self.lemmas = []
		self.postags = []
		self.relations = []
		self.text = []

class TextHandler(ContentHandler):
    
    in_text = False
    
    def __init__(self, text):
        ContentHandler.__init__(self)
        self.text = text
        self.data = []
        
    def startElement(self, name, attrs):
        if name == "text":
         	self.in_text = True
            	
    def endElement(self, name):
       	if name == "text":
      		t = ''.join(self.data)
       		self.data = []
       		self.text.append(t)
       		self.in_text = False
       		
    def characters(self, string):
       	if self.in_text:
       		self.data.append(string)
        		


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
#			if name == "word":
#				self.hypothesis[self.index].words.append(name)
			if name == "lemma":
				self.in_lemma = True
#				self.hypothesis[self.index].lemmas.append(name)
			if name == "pos-tag":
				self.in_pos = True
#				self.hypothesis[self.index].postags.append(name)
#			if name == "relation":
#				self.hypothesis[self.index].relations.append(name)
	
	def endElement(self, name):
		if name == "hypothesis":
			self.passthrough = False
			self.in_word = False
			t = ''.join(self.data)
			self.data = []
			self.hypothesis[self.index].text.append(t)
			l = ''.join(self.lemma)
			p = ''.join(self.pos)
			self.lemma = []
			self.pos = []
			self.hypothesis[self.index].lemmas.append(l)
			self.hypothesis[self.index].postags.append(p)
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
	
#	in_hypothesis = False
#	in_word = False
#	in_lemma = False
#	in_pos_tag = False
#	in_relation = False
#	index = 0
#	
#	def __init__(self, hypothesis):
#		ContentHandler.__init__(self)
#		self.hypothesis = hypothesis
#		self.data = []
#		self.hypothesis.append(Hypothesis())
#		
#	def startElement(self, name, attrs):
#		if name == "hypothesis":
#			self.in_hypothesis = True
#			self.hypothesis.append(Hypothesis())
#		elif name == "word":
#			self.in_word = True
#		elif name == "lemma":
#			self.in_lemma = True
#		elif name == "pos-tag":
#			self.in_pos_tag = True
#		elif name == "relation":
#			self.in_relation = True
#			
#	def endElement(self, name):
#		if name == "hypothesis":
#			t = ''.join(self.data)
#			self.data = []
#			self.hypothesis[self.index].text.append(t)
#			self.in_hypothesis = False
#			self.index += 1
#		elif name == "word":
#			t = ''.join(self.data)
#			self.data = []
#			self.hypothesis[self.index].words.append(t)
#			self.in_word = False
##			self.hypothesis.words.append(name)
#		elif name == "lemmas":
#			t = ''.join(self.data)
#			self.data = []
#			self.hypothesis[self.index].lemmas.append(name)
#			self.in_lemma = False
#		elif name == "pos-tags":
#			t = ''.join(self.data)
#			self.data = []
#			self.hypothesis[self.index].pos-tags.append(name)
#			self.in_pos_tag = False
#		elif name == "relations":
#			t = ''.join(self.data)
#			self.data = []
#			self.hypothesis[self.index].relations.append(name)
#			self.in_relation = False
#			
#	def characters(self, string):
#		if self.in_hypothesis or self.in_word or self.in_lemma or self.in_pos_tag or self.in_relation:
#			self.data.append(string)
			
			
text = []
hypothesis = []
parse("RTE2_dev.preprocessed.xml", TextHandler(text))
parse("RTE2_dev.preprocessed.xml", HypothesisHandler(hypothesis))

print len(text)
print len(hypothesis)
h = hypothesis[0]
l = h.lemmas[0]
p = h.postags[0]
l = l.split('\t')
l = map(lambda x : x.strip('.,:;"'), l)
l = sorted(set(l))
print l
