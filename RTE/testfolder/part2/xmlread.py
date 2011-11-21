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
		
file = open("RTE2.txt")

texts = []
hypos = []
words = []
index = -1
xml = file.read()
in_text = False
in_hypo = False

xml = xml.split("'")
xml = filter(lambda x : x[0] != ",", xml)
xml = filter(lambda x : x[0] != ".", xml)
xml = filter(lambda x : x[0] != "-", xml)
xml = filter(lambda x : not x.startswith("</"), xml)
for i in range(len(xml)):
	if xml[i] == "<text>":
		in_text = True
		in_hypo = False
		index += 1
		texts.append(Text())
		continue
	if xml[i] == "<word>" and not xml[i+1].startswith("<") and in_text:
		texts[index].words.append(xml[i+1])
	elif xml[i] == "<lemma>" and not xml[i+1].startswith("<") and in_text:
		texts[index].lemmas.append(xml[i+1])
	elif xml[i] == "<pos-tag>" and not xml[i+1].startswith("<") and in_text:
		texts[index].pos.append(xml[i+1])
	if xml[i] == "<hypothesis>":
		in_text = False
		
index = -1
for i in range(len(xml)):
	if xml[i] == "<hypothesis>":
		in_hypo = True
		index += 1
		hypos.append(Hypothesis())
		continue
	if xml[i] == "<word>" and not xml[i+1].startswith("<") and in_hypo:
		hypos[index].words.append(xml[i+1])
	elif xml[i] == "<lemma>" and not xml[i+1].startswith("<") and in_hypo:
		hypos[index].lemmas.append(xml[i+1])
	elif xml[i] == "<pos-tag>" and not xml[i+1].startswith("<") and in_hypo:
		hypos[index].pos.append(xml[i+1])
	if xml[i] == "<text>":
		in_hypo = False
		
print len(texts), len(hypos)
print texts[5].words, hypos[5].words, hypos[5].pos
		
