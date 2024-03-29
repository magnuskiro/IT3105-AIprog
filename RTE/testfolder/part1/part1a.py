#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 2011 Jan Alexander Stormark Bremnes & Magnus Kirø

from xml.sax.handler import ContentHandler
from xml.sax import parse
import predict
import part1c
import part1d

line_no = 0

#***********************************************************
# Example class - prints all the tags in the xml/html file 
#***********************************************************	

#class TestHandler(ContentHandler):
#	def startElement(self, name, attrs):
#		print name, attrs.keys()
#parse('RTE2_dev.xml', TestHandler())


#***********************************************************	
# Extracts the text enclosed in <t></t> 		   
# Returns a list of characters				   
#***********************************************************	

class TextHandler(ContentHandler):
	
	in_text = False
	
	def __init__(self, text):
		ContentHandler.__init__(self)
		self.text = text
		self.data = []
		
	def startElement(self, name, attrs):
		if name == 't':
			self.in_text = True
			
	def endElement(self, name):
		if name == 't':
			t = ''.join(self.data)
			self.data = []
			self.text.append(t)
			self.in_text = False
			
	def characters(self, string):
		if self.in_text:
			self.data.append(string)


#***********************************************************	
# Extracts the text enclosed in <h></h> 		   
# Returns a list of characters                             
#***********************************************************		
		
class HypothesisHandler(ContentHandler):
	
	in_hypothesis = False
	
	def __init__(self, hypothesis):
		ContentHandler.__init__(self)
		self.hypothesis = hypothesis
		self.data = []
		
	def startElement(self, name, attrs):
		if name == 'h':
			self.in_hypothesis = True
			
	def endElement(self, name):
		if name == 'h':
			t = ''.join(self.data)
			self.data = []
			self.hypothesis.append(t)
			self.in_hypothesis = False
			
	def characters(self, string):
		if self.in_hypothesis:
			self.data.append(string)
		


# Uses the content handlers to extract texts and hypothesis from the xml-file				   
text = []
hypothesis = []
parse("RTE2_dev.xml", TextHandler(text))
parse("RTE2_dev.xml", HypothesisHandler(hypothesis))

print len(text)

# converts everything to lowercase
text = map(lambda x : x.lower(), text)
hypothesis = map(lambda x : x.lower(), hypothesis)

no_words = []
texts = []
hypos = []
# TODO: creating lists of words and removal of punctuation can be done on the text-list as awhole
# 	instead of for each element
for i in range(len(text)):
	t = text[i]
	h = hypothesis[i]
	
	# create lists of words from the lists of characters
	t = t.split()				
	h = h.split()

	# remove punctuations TODO: Extend the list of characters to be removed
	t = map(lambda x : x.strip('.,:;()"'), t)	
	h = map(lambda x : x.strip('.,:;()"'), h)
	
	if i == 500:
		print i
		print t
		print h
	texts.append(t)
	hypos.append(h)
	
	t = sorted(t)
	h = sorted(h)

	
	# extracts words with regex, 
	# t = re.findall(r"[a-zA-Z']+", t)
	
	# counts the number of words that occur in both text and corresponding hypothesis 	
	x = 0
	for j in h:
		if j in t:
			x += 1
	no_words.append(x)

# Calculates a normalized value for the number of words occuring in both text and hypothesis
word_match = []
for i in range(len(no_words)):
	h = hypothesis[i]
	h = h.split()
	h = map(lambda x : x.strip('.,:;"'), h)
	h = sorted(h)
	word_match.append((no_words[i]*1.0) / len(h))

# Prints the list of word matches to file
out = "wordmatches.txt"
file = open(out, 'wb')
if file:
	for i in word_match:
		print >> file, i
	file.close()
else:
	print "Error opening file"
 
# Call predict with step_size and wordmatches to find best threshold 	
step_size = 0.001
name = "wordmatches.txt" 
bleu = "bleuresults.txt"	
idf = "idfresults.txt"
#predict.predict(step_size, name)
#part1c.run(texts, hypos)
predict.predict(step_size, bleu)
part1d.predict(texts, hypos)
predict.predict(step_size, idf)

