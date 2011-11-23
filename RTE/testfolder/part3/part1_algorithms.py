#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 2011 Jan Alexander Stormark Bremnes & Magnus Kirø

def clean(text):
    return text.strip(',. :;"')

def word_matching(text,hypo):
    text_words = [clean(t) for t in text.lower().split()]
    hypo_words = [clean(h) for h in hypo.lower().split()]
    word_counter = 0
    for h in hypo_words:
        if h in text_words:
            word_counter += 1
    return float(word_counter) / len(hypo_words)

def lemma_matching(text, hypo):
    lem_text = [n.lemma for s in text for n in s.nodes if n.isWord]
    lem_hypo = [n.lemma for s in hypo for n in s.nodes if n.isWord]
    hyp_in_text = filter(lambda x: x in lem_text, lem_hypo)
    return float(len(hyp_in_text)) / len(lem_hypo)


def lemma_pos_matching(text, hypo):
    lem_text = [(n.lemma,n.postag) for s in text for n in s.nodes if n.isWord]
    lem_hypo = [(n.lemma,n.postag) for s in hypo for n in s.nodes if n.isWord]
    hyp_in_text = filter(lambda x: x in lem_text, lem_hypo)
    return float(len(hyp_in_text)) / len(lem_hypo)


def bigram_matching(text,hypo):
    t = list(ngrams(text,2))
    h = list(ngrams(hypo,2))
    counter = 0
    for w in h:
        if w in t:
            counter += 1
    return float(counter) / len(h)


def ngrams(texts,n):
    i = 0
    while i + n <= len(texts):
        yield tuple(texts[i:i+n])
        i += 1
