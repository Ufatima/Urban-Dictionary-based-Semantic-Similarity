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


stop = set(stopwords.words('english'))
model = gensim.models.KeyedVectors.load_word2vec_format('./models/GoogleNews-vectors-negative300.bin', binary=True)

def compute_distance(ss1, ss2):
    count = 0
    tempsum = 0.0
    for i_index, i in enumerate(ss1.lower().split()):
        i = i.strip()
        i = i.strip(string.punctuation)
        try:
            if i in model and i not in stop:
                temparray = []
                count_j = 0
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
                            count_j += 1
                    except:
                        print("Unexpected error:", sys.exc_info()[0])
                #print(count_j)
                tempsum = tempsum + max(temparray)
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
                s1 = sentencesp1[d1]
                s2 = sentencesp2[d2]
                sim1 = compute_distance(s1, s2)
                sim2 = compute_distance(s2, s1)
                sim = (sim1+sim2)/2.0
                m.append(sim)
        #print(m)
        #         n = [definition_1, definition_2, sim]
        #         s.append(n)
        # a = np.array(s)
        # with open('millar_wordsim.csv', 'w', newline="") as f:
        #     writer = csv.writer(f)
        #     writer.writerows(a)
        if len(m):
            a = np.max(m)
            print(a)
        else:
            a = 0.0
            print(a)
        m = []
