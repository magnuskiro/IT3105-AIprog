from xml.etree.cElementTree import parse as xml_parser
from xml.etree.cElementTree import parse as xmlparse


class Pair(object):
    def __init__(self, t):
        self.id = t.attrib['id'].strip()
        self.task = t.attrib['task'].strip()
        self.text = [Sentence(s) for s in t.getiterator('text/sentence')]
        self.hypothesis = [Sentence(s) for s in t.getiterator('hypothesis/sentence')]
        self.entailment = t.attrib['entailment']

class Sentence(object): # list of nodes
    def __init__(self, t):
        self.serial = t.attrib['serial'].strip()
        self.nodes = [Node(n) for n in t.getiterator('node')]

class Node(object):
    def __init__(self, t): # t = the etree containing containing data.
        self.id = t.attrib['id']
        if self.id[0] == 'E': # artificial node
            self.isWord = False
        else:
            self.isWord = True
            self.word = t.findtext('word').strip()
            self.lemma = t.findtext('lemma').strip()
            self.postag = t.findtext('pos-tag').strip()
            self.relation = t.findtext('relation')
            if self.relation: self.relations = self.relation.strip()
"""
def parse_preprocessed_xml(pre_data):
    tree = xml_parser(pre_data)
    pairs = []
    for pair in tree.iterfind('pair'):
        pairs.append(Pair(pair))
    return pairs
"""
def parse_preprocessed_xml(fileh):
    etree = xmlparse(fileh)
    pairs = []
    for pair in etree.getiterator("pair"):
        pairs.append(Pair(pair))
    return pairs

pre_data = parse_preprocessed_xml("../xml/RTE2_dev.preprocessed.xml")
print pre_data