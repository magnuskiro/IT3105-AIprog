#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 2011 Jan Alexander Stormark Bremnes & Magnus Kirø

#import os
import argparse
import eval_rte

# Reads the list of word matches, and prints to file a list of predictions in RTE output format                   
def predict(threshold, name):
	file = open(name)
	c = []
	threshold = threshold
	if file:
		for line in file:
			c.append(float(line))
		file.close()
	else:
		print "Error opening file"
	
	file_name = "prediction_"+name
	out = file_name
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


