#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 2011 Jan Alexander Stormark Bremnes & Magnus Kirø


# acquires the features from part one and two.

from data_processing import parse_xml, parse_preprocessed_xml
from part1_algorithms import word_matching, lemma_matching, lemma_pos_matching, bigram_matching

def write(text):
    filename = "learningdata.tab"
    file = open(filename, 'a')
    if file:
        file.write(str(text))
    else:
        print "Error opening file"
    file.close()

def feature_extraction(pre_data,dev_data):
    write('id\tword\tlemma\tpos\tbigrams\tentailment\t\n')
    write('d\tc\tc\tc\tc\td\n')
    write('meta\t\t\t\t\tclass')
    for pair in pre_data:
        write("\n")
        write(pair.id)
        text = dev_data[pair.id][1]
        hypo = dev_data[pair.id][2]
        #print text, hypo
        write("\t")
        write(word_matching(text,hypo)) #done
        write("\t")
        write(lemma_matching(pair.text, pair.hypo)) #
        write("\t")
        write(lemma_pos_matching(pair.text, pair.hypo)) #
        write("\t")
        write(bigram_matching(text,hypo)) #
        write("\t")
        write(dev_data[pair.id][0]['entailment']) # done

def clean_file():
    file = open("learningdata.tab", "wb")
    file.write("")
    file.close()

def run(dev_data_file="../xml/RTE2_dev.xml", pre_data_file="../xml/RTE2_dev.preprocessed.xml"):
    clean_file()
    print "start feature extraction"
    # remember to change path to xml files when changing folders. 
    dev_data = parse_xml(dev_data_file)
    #print dev_data
    pre_data = parse_preprocessed_xml(pre_data_file)
    #print pre_data
    print "Extracting Features"
    feature_extraction(pre_data, dev_data)
    print "Done"

#run()
