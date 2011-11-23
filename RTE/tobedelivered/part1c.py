#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2011 Magnus Kirø & Jan Alexander Stormark Bremnes

# pseudo code
# see EnrDiaPascal05.pdf
#1:
    # for several values of N (1-4) 
    #     calculate the percentage of n-grams from the candidate
    #        translation wich appears in any of the human translations. 
    #        The frequency of each n-grams is limited to the maximum
    #        frequency with which it appears in any reference. 
#2:
    # Combine the marks obtained for each value of N, 
    #    as a weighted linear average
#3:
    # Apply a brevity factor to penalise short candidate texts 
    # (which may have n-grams in common with the reference, but may be incomplete).
    # If the candidate is shorter than the references, this factor is calculated
    # as the ratio between the length of the candidate 
    # which has the most similar length.
#

# TODO:iterate and calculate threshold 
# print out YES/NO for the given probability. 

from math import e

# TODO: is this the correct way to do it?
# Number of n-grams and the size of the largest n-gram.  
# Largest n-gram is entire hypothesis, or text is hypo > text   
number_of_ngrams = 4
threshold = 0

def bleu(T, H):
#	H = clean(H)
#	T = clean(T)
	global number_of_ngrams
	if len(H) < number_of_ngrams:
		number_of_ngrams = len(H)
	else:
		number_of_ngrams = 4
		
	result = evaluateTH(T, H)
	return result

#Given T(ext) and H(ypothesis)
def evaluateTH(T, H):
	
	# find the probability based on n-gram
	probs = [0]*number_of_ngrams
	for N in range(1, number_of_ngrams+1):
		probs[N-1] = calcNgram(T, H, N)
	
	probsum = 0
	for i in range(len(probs)):
		probsum += probs[i]
	totprob = (1.0/number_of_ngrams) * probsum
	return totprob

#def evaluateTH(T, H):

#	file = open("bleuresults.txt", "wb")
#	#find the probability based on n-gram
#	probs = [0]*number_of_ngrams
#	for N in range(1, number_of_ngrams+1):
#		probs[N-1] = calcNgram(T, H, N)
#    #find total matching probability for H  in T.
#    # formula taken from the lecture notes. 
#    
##   print probs
#    probsum = 0
#    for i in range(len(probs)):
#        probsum += probs[i]
#    totprob = (1.0/number_of_ngrams) * probsum

#	if file:
#	    print >>, file, totprob
#	else:
#		print "Error opening file"
#	file.close()
    
#return the probability of n-gram in T. 
def calcNgram(T, H, N):

    #use H/T to create corpie of size N.
    hgrams = textSplit(H, N)
    tgrams = textSplit(T, N)
    
#    # for debugging
#    print tgrams
#    print hgrams
    
    # counts the number of n-grams that appear both in T and H
    m = 0
    for n_gram in hgrams:
    	if n_gram in tgrams:
    		m += 1	
    
    # calculate probability
    # m = number of n-grams that are found in both T and H
    # w = total number of n-grams in H
    w = len(hgrams)
    prob = 0
    if m > 0:
    	prob = (m*1.0)/w
    
    # probability of correctness 
    return prob

# Sanitizes the given text and splits into lowercase words
# Returns a list of the words in the text, without special characters    
def clean(dirty):
	# remove unwanted characters
	clean = map(lambda x : x.strip("?.,"), dirty)

	# convert all text to lowercase
	clean = "".join(clean)
	clean = clean.lower()
	
	# join characters into words
	clean = clean.split(" ")
	return clean
	
	
#creates the n-grams to be compared. 
def textSplit(text, N):
    n_grams = []
    length = len(text) - N + 1
    #length = length -N -1 #removes N because we want an n-gram of length N. Removes 1 because of 0 index. 
    for i in range(length):
    	n_grams.append("") 
        for j in range(N):
        	n_grams[i] += " " + text[i+j]
    return n_grams
    
def corpusInT(T, corpus):
    for c in T:
        if c == corpus:
            return True
    return False
    
## For testing
#a = "hallo alle sammen, jeg er Mr. Melk, hvordan henger den?"
#b = "Mr. Melk snakket nettop til deg"
#bleu(a,b)

def run(texts, hypos):
	file = open("bleuresults.txt", "wb")
	if file:
		for i in range(len(texts)):
			result = bleu(texts[i], hypos[i])
			print >> file, result
	else:
		print "Error opening file"
	file.close()

#1d:
#Consider a document containing 100 words wherein 
#the word cow appears 3 times. Following the previously 
#defined formulas, the term frequency (TF) for cow is then (3 / 100) = 0.03. 
#Now, assume we have 10 million documents and cow appears in one 
#thousand of these. Then, the inverse document frequency is calculated 
#as log(10 000 000 / 1 000) = 4. The tf–idf score is the product of these 
#quantities: 0.03 × 4 = 0.12.
