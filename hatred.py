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

from nltk.corpus import stopwords
stop = set(stopwords.words('english'))
model = gensim.models.KeyedVectors.load_word2vec_format('./models/GoogleNews-vectors-negative300.bin', binary=True)

def cos_similarity(ss1, ss2):
    count = 0
    tempsum = 0.0
    for i_index, i in enumerate(ss1.lower().split()):
        i = i.strip()
        i = i.strip(string.punctuation)
        try:
            if i in model and i not in stop:
                temparray = []
                for j_index, j in enumerate(ss2.lower().split()):
                    j = j.strip()
                    j = j.strip(string.punctuation)
                    try:
                        if j in model and j not in stop:
                            vec1 = model.wv[i]
                            vec2 = model.wv[j]
                            numerator = np.dot(vec1, vec2)
                            denominator = (sqrt(np.dot(vec1, vec1)) * sqrt(np.dot(vec2, vec2)))
                            cos_similarity = numerator / denominator
                            temparray.append(cos_similarity)
                    except:
                        print("Unexpected error:", sys.exc_info()[0])
                tempsum = tempsum + max(temparray)
                count += 1
        except:
            print("Unexpected error:", sys.exc_info()[0])
    if count == 0:
        return 0
    else:
        return (tempsum / count)
with open ("rg_word.csv", "r") as mfile:
    for line in mfile:
        linesp = line.split(",")
        term1 = linesp[0]
        term2 = linesp[1]
        #print(term1,term2)
        def1 = ud.define(linesp[0])
        def2 = ud.define(linesp[1])
        ul1 = []
        ul2 = []
        sentence1 = []
        sentence2 = []
        for d in def1:
            unlike1 = d.downvotes
            ul1.append(unlike1)
        for d in def2:
            unlike2 = d.upvotes
            ul2.append(unlike2)
        if len(ul1) != 0:
            if len(ul2) != 0:
                maxul1 = max(ul1)
                maxul2 = max(ul2)
                #print(maxul1,maxul2)
                s1 = []
                s2 = []
                for p in def1:
                    s = p.definition
                    s1.append(s)
                for q in def2:
                    ss = q.definition
                    s2.append(ss)

                for j in range(len(s1)):
                    sen1 = s1[j]
                    if ul1[j] == maxul1:
                        #print(s1[j])
                        n = s1[j]
                        sentence1.append(n)
                for k in range(len(s2)):
                    sen2 = s2[k]
                    if ul2[k] == maxul2:
                        #print(s2[k])
                        m = s2[k]
                        sentence2.append(m)
        for d1 in range(len(sentence2)):
            ss1 = sentence1[d1]
            ss2 = sentence2[d1]
            sim1 = cos_similarity(ss1, ss2)
            sim2 = cos_similarity(ss2, ss1)
            sim = (sim1 + sim2) / 2.0
            print(sim)