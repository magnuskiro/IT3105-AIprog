#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import os
import argparse
import eval_rte

def predict(step_size, name):
	step_size = float(step_size)
	# Reads the list of word matches, and prints to file a list of predictions in RTE output format                   
	file = open(name)
	c = []
	threshold = 0
	best_match = 0
	match_threshold = 0
	if file:
		for line in file:
			c.append(float(line))
		file.close()
	else:
		print "Error opening file"
	
	while threshold < 1:
		threshold = threshold + step_size
		out = "predictions.txt"
		file = open(out, 'wb')
		if file:
			print >> file, "ranked: no"
	
			for i in range(len(c)):
				if c[i] > threshold:
					print >> file, i+1, "YES"
				else:
					print >> file, i+1, "NO"
			file.close()
		else:
			print "Error opening file" 
		match = eval_rte.evaluate("RTE2_dev.xml", "predictions.txt")
		if match > best_match:
			best_match = match
			match_threshold = threshold
		
	print "%.4f" %best_match, "%.4f" %match_threshold
		
#parser = argparse.ArgumentParser(description="increment by this value")
#parser.add_argument("step_size", help="value that threshold shall be incremented with")
#args = parser.parse_args()
#evaluate(args.step_size)
#os.system("./eval_rte.py RTE2_dev.xml predictions.txt")


