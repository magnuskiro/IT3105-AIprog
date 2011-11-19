# -*- coding: utf-8 -*-
# calculate IDF for every word in the document collection: text and hypothesis. 
# extend word matching strategy from the first system by wheighting each word according to its IDF value. 
# iterate to find a threshold. 


# IDF weight of a word is simply the inverse of the number of documents that the word appears in

#IDF calculation. 
#IDF = log ( number of ducuments / number of instances of the given word ) 

#use the IDF values to decide YES/NO for a hypo. 
    #IDF word match. 
#IDF Word Match = ( sum IDF(w) where w in (T and H) )/( sum IDF(w) where w in H ) # total word match for H in T. 
     
from math import log

"""
def IDF(word, collection):
    probValue = 0
    num = 0
    for item in collection[0]: 
        if item == word:
            num+=1
    for item in collection[1]:
        if item == word:
            num+=1
    #IDF = log ( number of ducuments / number of instances of the given word )    
    probValue = log(2 / num)
    print probValue
    return probValue
"""

def IDFwordMatch(text, hypo, IDFdict):
    collection = text + hypo
    hypwords = hypo    
    #IDF Word Match = ( sum IDF(w) where w in (T and H) )/( sum IDF(w) where w in H ) # total word match for H in T.
    sum1 = 0
    for w in collection:
        sum1+=IDFdict[w]

    sum2 = 0
    for w in hypwords:
        sum2+=IDFdict[w]

    totprob = sum1/sum2
    return totprob

#def predict(texts, hypos): 
#    for n in range(len(texts)):
#        print IDFwordMatch(texts[n], hypos[n])
    #print IDFwordMatch(texts[2], hypos[2])

    
### TO be used ###
#1600 dokumenter = 1600 set med ord.  == document collection
# gjør alle dokumenter om til set. 
# finn allWords = settet med alle orda i document collection.
# for alle orda i allWords calc IDF og put det i et dictionary.  

# IDF word match. hent verdien fra et dictionary. 


def predict(texts, hypos):
    IDFdict = createWordIDFs(texts, hypos)
    for n in range(len(texts)):
        print IDFwordMatch(texts[n], hypos[n], IDFdict)
    print "done"

def createWordIDFs(texts, hypos):
    allwords=[]
    texts_set = texts[:]
    hypos_set = hypos[:]
    for n in range(len(texts)):
        allwords+=texts[n]
        texts_set[n]=set(texts[n])
        allwords+=hypos[n]
        hypos_set[n]=set(hypos[n])
    allwords=set(allwords)
#    print len(allwords)
#    print allwords
#    print IDF("it", texts, hypos)
    IDFdict = {}
    for word in allwords:
        IDFdict[word] = IDF(word, texts_set, hypos_set)
#        print IDFdict[word]
    return IDFdict

def IDF(word, texts, hypos):
    count = 0; 
    for n in range(len(texts)):
        if word in hypos[n]:
            count+=1 
        if word in texts[n]:
            count+=1
#    print count
    return (1*1.0)/count #recommended IDF
#    return log( (len(texts)+len(hypos)) / count) #found IDF calculation from the wikipedia and others. 




