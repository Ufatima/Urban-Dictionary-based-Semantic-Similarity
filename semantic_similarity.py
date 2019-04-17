import gensim
import urbandictionary as ud
from gensim import corpora, models, similarities
from gensim.models.word2vec import Word2Vec
import numpy as np
from nltk.corpus import stopwords
import sys
import pandas as pd
import string
from string import punctuation
from math import *
import csv
from sematch.semantic.similarity import WordNetSimilarity

wns = WordNetSimilarity()
stop = set(stopwords.words('english'))
model = gensim.models.KeyedVectors.load_word2vec_format('./models/GoogleNews-vectors-negative300.bin', binary=True)

def sem_similarity(s1, s2):
    count = 0
    tempsum = 0.0
    for i_index, i in enumerate(s1.lower().split()):
        i = i.strip()
        i = i.strip(string.punctuation)

        i = i.replace("'", "")  # removed apostrophes
        try:
            if i not in stop:
                temparray = []
                for j_index, j in enumerate(s2.lower().split()):
                    j = j.strip()
                    j = j.strip(string.punctuation)
                    j = j.replace("'", "")  # removed apostrophes
                    try:
                        if j not in stop:
                            temparray.append(wns.word_similarity(i, j, 'lch'))
                    except:
                        print("Unexpected error:", sys.exc_info()[0])
                tempsum += max(temparray)
                count += 1
        except:
            print("Unexpected error:", sys.exc_info()[0])
    if count == 0:
        return 0
    else:
        return (tempsum / count)
m = []
with open("rg_word.csv", "r") as f:
    s = []
    for line in f:
        linesp = line.split(',')
        def1 = ud.define(linesp[0])
        def2 = ud.define(linesp[1])
        sentencesp1 = []
        for d in def1:
            s1 = d.definition
            sentencesp1.append(s1)
        sentencesp2 = []
        for d in def2:
            s2 = d.definition
            sentencesp2.append(s2)
        for d1 in range(len(sentencesp1)):
            for d2 in range(len(sentencesp2)):
                cosine = 0.0
                definition_1 = sentencesp1[d1]
                definition_2 = sentencesp2[d2]
                sim1 = sem_similarity(definition_1, definition_2)
                sim2 = sem_similarity(definition_1, definition_2)
                sim = (sim1 + sim2)/2.0
                m.append(sim)
        if len(m):
            a = np.max(m)
            print(a)
        else:
            a = 0.0
            print(a)
        m = []
