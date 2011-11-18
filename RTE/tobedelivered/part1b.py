#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 2011 Jan Alexander Stormark Bremnes & Magnus Kirø

# TODO: ATTENTION! This part is perhaps not complete! Need to
# find out if matching should be done on lemma + pos-tag, or
# just pos-tag. 

from xml.sax.handler import ContentHandler
from xml.sax import parse
import predict

line_no = 666

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
	in_word = False
	index = 0    
	
	def __init__(self, text):
		ContentHandler.__init__(self)
		self.text = text
		self.data = []
		self.lemma = []
		self.pos = []
		self.word = []
		
	def startElement(self, name, attrs):
		if name == "text":
			self.passthrough = True
			self.text.append(Text())
		elif self.passthrough:
			if name == "lemma":
				self.in_lemma = True
			if name == "pos-tag":
				self.in_pos = True
			if name == "word":
				self.in_word = True
	
	def endElement(self, name):
		if name == "text":
			self.passthrough = False
			l = ''.join(self.lemma)
			p = ''.join(self.pos)
			w = ''.join(self.word)
			self.lemma = []
			self.pos = []
			self.word = []
			self.text[self.index].lemmas.append(l)
			self.text[self.index].pos.append(p)
			self.text[self.index].words.append(w)
			self.index += 1
		if name == "lemma":
			self.in_lemma = False
		if name == "pos-tag":
			self.in_pos = False
		if name == "word":
			self.in_word = False
	
	def characters(self, string):
		if self.in_lemma:
			self.lemma.append(string)
		if self.in_pos:
			self.pos.append(string)
		if self.in_word:
			self.word.append(string)
    

#***********************************************************	
# Parses the xml-file and extracts the lemmas and pos-tags		   
# found between <hypothesis></hypothesis> and creates a 
# hypothesis object for each hypothesis found
#***********************************************************
class HypothesisHandler(ContentHandler):
	
	passthrough = False
	in_lemma = False
	in_pos = False
	in_word = False
	index = 0
	
	def __init__(self, hypothesis):
		ContentHandler.__init__(self)
		self.hypothesis = hypothesis
		self.data = []
		self.lemma = []
		self.pos = []
		self.word = []
		
	def startElement(self, name, attrs):
		if name == "hypothesis":
			self.passthrough = True
			self.hypothesis.append(Hypothesis())
		elif self.passthrough:
			if name == "lemma":
				self.in_lemma = True
			if name == "pos-tag":
				self.in_pos = True
			if name == "word":
				self.in_word = True
	
	def endElement(self, name):
		if name == "hypothesis":
			self.passthrough = False
			l = ''.join(self.lemma)
			p = ''.join(self.pos)
			w = ''.join(self.word)
			self.lemma = []
			self.pos = []
			self.word = []
			self.hypothesis[self.index].lemmas.append(l)
			self.hypothesis[self.index].pos.append(p)
			self.hypothesis[self.index].words.append(w)
			self.index += 1
		if name == "lemma":
			self.in_lemma = False
		if name == "pos-tag":
			self.in_pos = False
		if name == "word":
			self.in_word = False
	
	def characters(self, string):
		if self.in_lemma:
			self.lemma.append(string)
		if self.in_pos:
			self.pos.append(string)
		if self.in_word:
			self.word.append(string)
			
# Uses the content handlers to extract texts and hypothesis from the xml-file				   			
text = []
hypothesis = []
parse("RTE2_dev.preprocessed.xml", TextHandler(text))
parse("RTE2_dev.preprocessed.xml", HypothesisHandler(hypothesis))

# Just to check that all text and hypothesis entries have been processed
print len(text)
print len(hypothesis)

def remove(a):
	b = []
	for i in a:
		if len(i) > 0:
			b.append(i)
	return b
	
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


lemmas = []
pos = []
no_lemmas = []
no_pos = []
t_p_ls = []
h_p_ls = []
for i in range(len(text)):
    # Get the first text and hypothesis, then their lemmas and pos-tags
    t = text[i]
    h = hypothesis[i]
    t_lemmas = t.lemmas[0]
    t_pos = t.pos[0]
    t_words = t.words[0]
    h_lemmas = h.lemmas[0]
    h_pos = h.pos[0]
    h_words = h.words[0]
	
    # Remove tabs
    t_lemmas = t_lemmas.split()
    t_pos = t_pos.split()
    t_words = t_words.split()
    h_lemmas = h_lemmas.split()
    h_pos = h_pos.split()
    h_words = h_words.split()
    
    # Convert everything to lower case
    t_lemmas = map(lambda x : x.lower(), t_lemmas)
    t_pos = map(lambda x : x.lower(), t_pos)
    t_words = map(lambda x : x.lower(), t_words)
    h_lemmas = map(lambda x : x.lower(), h_lemmas)
    h_pos = map(lambda x : x.lower(), h_pos)
    h_words = map(lambda x : x.lower(), h_words)

	# Generate pos-tag/word-pairs
    t_p_l = create_pos_lemma(t_pos, t_lemmas)
    h_p_l = create_pos_lemma(h_pos, h_lemmas)
    
    # Append to list of pos-tags for every text/hypothesis
    t_p_ls.append(t_p_l)
    h_p_ls.append(h_p_l)
    
    # Remove newlines, punctuations and duplicates TODO: Are duplicates wanted or unwanted?
    t_lemmas = map(lambda x : x.strip('.,:;"~-'), t_lemmas)
    t_pos = map(lambda x : x.strip('.,:;"~-'), t_pos)
    t_words = map(lambda x : x.strip('.,:;"~-'), t_words)
    h_lemmas = map(lambda x : x.strip('.,:;"~-'), h_lemmas)
    h_pos = map(lambda x : x.strip('.,:;"~-'), h_pos)
    h_words = map(lambda x : x.strip('.,:;"~-'), h_words)
    
    # Remove empty characters
    t_lemmas = remove(t_lemmas)
    t_pos = remove(t_pos)
    t_words = remove(t_words)
    h_lemmas = remove(h_lemmas)
    h_pos = remove(h_pos)
    h_words = remove(h_words)
    
    # Append the lemmas to list of lemmas for every text/hypothesis
    lemmas.append(h_lemmas)
    pos.append(h_pos)
    
# For debugging
#    if i == line_no:
#    	print len(h_lemmas), len(h_pos)
    
    # Counts lemmas that occur in both text and hypothesis
    x = 0
    for l in h_lemmas:
    	if l in t_lemmas:
    		x += 1
    no_lemmas.append(x)

	# Count pos-tags/word-combinations that occur in both text and hypothesis
    x = 0
    for p in h_p_l:
    	if p in t_p_l:
    		x += 1
    no_pos.append(x)
    
    if i == line_no:
    	print h_p_l
    	print t_p_l

# For debugging
#print len(t_p_ls), len(h_p_ls)
#print t_p_ls[line_no], h_p_ls[line_no]
#print lemmas[line_no]

# Calculate normalized values for lemma and pos-tag matching
lemma_match = []
pos_match = []
#print no_lemmas
for i in range(len(lemmas)):
	lemma_match.append((no_lemmas[i]*1.0) / len(lemmas[i]))
	pos_match.append((no_pos[i]*1.0) / len(h_p_ls[i]))

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
step_size = 0.001
predict.predict(step_size, lemma_name)
predict.predict(step_size, pos_name)
    
