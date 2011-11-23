import part1d
import part1c
import predict
from xml.sax.handler import ContentHandler
from xml.sax import parse

def run(dev, processed):
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
	parse(dev, TextHandler(text))
	parse(dev, HypothesisHandler(hypothesis))

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

		texts.append(t)
		hypos.append(h)
	
	bleu = "bleuresults.txt"
	idf = "idfresults.txt"
	step_size = 0.001
	part1d.predict(texts, hypos)
	part1c.run(text, hypos)
	predict.predict(step_size, bleu)
	predict.predict(step_size, idf)
	

