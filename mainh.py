import gensim
import urbandictionary as ud
from gensim import corpora, models, similarities
from gensim.models.word2vec import Word2Vec
import numpy as np
from scipy import spatial
import math
from math import *
from nltk.corpus import stopwords
import csv
import pandas as pd
model = gensim.models.KeyedVectors.load_word2vec_format('./models/GoogleNews-vectors-negative300.bin', limit=500000, binary=True)


def avg_feature_vector(words, model, num_features, index2word):
    featureVec = np.zeros((num_features,), dtype="float32")
    nwords = 0
    for word in words:
        if word in index2word:
            nwords = nwords + 1
            featureVec = np.add(featureVec, model[word])
    if (nwords > 0):
        featureVec = np.divide(featureVec, nwords)
    return featureVec


def get_cosine(sa1, sa2):
    numerator = np.dot(sa1, sa2)
    denominator = (sqrt(np.dot(sa1, sa1)) * sqrt(np.dot(sa2, sa2)))
    cos_similarity = numerator / denominator
    #def1_def2_similarity = 1 - spatial.distance.cosine(sa1, sa2)
    return cos_similarity


with open("rg_word.csv", "r") as f:
    for line in f:
        m = []
        linesp = line.split(',')
        def1 = ud.define(linesp[0])
        def2 = ud.define(linesp[1])
        print(linesp[0],linesp[1])
        sentencesp1 = []
        for d in def1:
            s1 = d.definition
            sentencesp1.append(s1)
        sentencesp2 = []
        for d in def2:
            s2 = d.definition
            sentencesp2.append(s2)
        matrix = np.zeros(shape=(len(sentencesp1), len(sentencesp2)))

        for d1 in range(len(sentencesp1)):
            for d2 in range(len(sentencesp2)):
                cosine = 0.0
                stop = set(stopwords.words('english'))
                definition_1 = sentencesp1[d1]
                for i in sentencesp1[d1].lower().split():
                    if i not in stop:
                        d1_avg_vector = avg_feature_vector(i, model, num_features=300,
                                                                     index2word=set(model.index2word))

                definition_2 = sentencesp2[d2]
                for i in sentencesp2[d2].lower().split():
                    if i not in stop:
                        d2_avg_vector = avg_feature_vector(i, model, num_features=300,
                                                                     index2word=set(model.index2word))
                matrix[d1][d2] = get_cosine(d1_avg_vector, d2_avg_vector)
        #print(matrix)
        df = pd.DataFrame(matrix)
        max_value = matrix.max()
        print(max_value)
        #np.savetxt('out.csv', matrix, delimiter=',', fmt='%1.11f')
