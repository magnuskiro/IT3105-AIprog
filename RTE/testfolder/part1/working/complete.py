#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 2011 Jan Alexander Stormark Bremnes & Magnus Kirø

import argparse
import eval_rte

bleu_threshold = 0.2690	
word_threshold = 0.8190
lemma_threshold = 0.9170 
pos_threshold = 0.5790

bleu_result = 0.5162
word_result = 0.5138
lemma_result = 0.5112
pos_result = 0.5250

sum_result = bleu_result+word_result+lemma_result+pos_result

bleu_result = bleu_result/sum_result
word_result = word_result/sum_result
lemma_result = lemma_result/sum_result
pos_result = pos_result/sum_result

sum_result = bleu_result+word_result+lemma_result+pos_result

print sum_result

bleu_result = bleu_result

def read_file(file):
	a = []
	if file:
		for line in file:
			a.append(float(line))
		return a
	else:
		print "Error opening file"
		return 0


def predict():
	
	# Reads the list of word matches, and prints to file a list of predictions in RTE output format                   
	b = open("bleuresults.txt")
	bleu = read_file(b)
	b.close()
	w = open("wordmatches.txt")
	word = read_file(w)
	w.close()
	l = open("lemma_matches.txt")
	lemma = read_file(l)
	l.close()
	p = open("pos-tag_matches.txt")
	pos = read_file(p)
	p.close()
	
	print len(bleu), len(word), len(lemma), len(pos)
	
	file = open("finalresult.txt", "wb")
	if file:
		print >> file, "ranked: no"	
		for i in range(len(bleu)):
			yes = 0
			no = 0
			if bleu[i] > bleu_threshold:
				yes += bleu_result
			elif bleu[i] < bleu_threshold:
				no += bleu_result
				
			if word[i] > word_threshold:
				yes += word_result
			elif word[i] < word_threshold:
				no += word_result
				
			if lemma[i] > lemma_threshold:
				yes += lemma_result
			elif lemma[i] < lemma_threshold:
				no += lemma_result
				
			if pos[i] > pos_threshold:
				yes += pos_result
			elif pos[i] < pos_threshold:
				no += pos_result
				
			if yes > no:
				print >> file, i+1, "YES"
			else:
				print >> file, i+1, "NO"
		file.close()
	else:
		print "Error opening file"
		
	match = eval_rte.evaluate("RTE2_dev.xml", "finalresult.txt")
	print "%.4f" %match
			
	
	
predict()
#	c = []
#	threshold = 0
#	best_match = 0
#	match_threshold = 0
#	if file:
#		for line in file:
#			c.append(float(line))
#		file.close()
#	else:
#		print "Error opening file"
#	
#	while threshold < 1:
#		threshold = threshold + step_size
#		out = "predictions.txt"
#		file = open(out, 'wb')
#		if file:
#			print >> file, "ranked: no"
#	
#			for i in range(len(c)):
#				if c[i] > threshold:
#					print >> file, i+1, "YES"
#				else:
#					print >> file, i+1, "NO"
#			file.close()
#		else:
#			print "Error opening file" 
#		match = eval_rte.evaluate("RTE2_dev.xml", "predictions.txt")
#		if match > best_match:
#			best_match = match
#			match_threshold = threshold
#		
#	print "%.4f" %best_match, "%.4f" %match_threshold
