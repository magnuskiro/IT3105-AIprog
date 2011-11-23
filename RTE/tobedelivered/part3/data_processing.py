#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 2011 Jan Alexander Stormark Bremnes & Magnus Kirø

from xml.etree.ElementTree import ElementTree
from xml.etree.cElementTree import parse as xml_parser

class Pair(object):
    def __init__(self, t):
        self.id = t.attrib['id'].strip()
        self.task = t.attrib['task'].strip()
        #print "pair!"
        #for s in t.findall('text/sentence'): print s.getiterator('node')
        self.text = [Sentence(s) for s in t.findall('text/sentence')]
        #print self.text
        self.hypo = [Sentence(s) for s in t.findall('hypothesis/sentence')]
        #print self.hypo
        #self.entailment = t.attrib['entailment'] # not needed in the feature extraction. as we do not know the entailment in the test data.

class Sentence(object): # list of nodes
    def __init__(self, t):
        self.serial = t.attrib['serial'].strip()
        self.nodes = [Node(n) for n in t.getiterator('node')] #getiterator is deprecated in python 2.7 use findall or similar. Not changed because I don't know what if it will work, which it does now.

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

def parse_xml(dev_data):
    tree = ElementTree()
    tree.parse(dev_data)
    parsed_pairs = {}
    #print "parse_xml"
    for pair in list(tree.findall('pair')):
        attrib = pair.attrib
        t = pair.find('t').text
        #print t
        h = pair.find('h').text
        #print h
        parsed_pairs[attrib['id']] = (attrib,t,h)
    return parsed_pairs

def parse_preprocessed_xml(pre_data):
    tree = xml_parser(pre_data)
    pairs = []
    for pair in tree.getiterator('pair'):
        pairs.append(Pair(pair))
    return pairs
