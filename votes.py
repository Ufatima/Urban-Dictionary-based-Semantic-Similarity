import urbandictionary as ud
from datetime import datetime, timedelta
import apscheduler
from apscheduler.schedulers.blocking import BlockingScheduler
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

from nltk.corpus import stopwords
stop = set(stopwords.words('english'))
model = gensim.models.KeyedVectors.load_word2vec_format('./models/GoogleNews-vectors-negative300.bin', binary=True)

# while 1:
#     with open("mc_wordpair.csv", "r") as mfile:
#         for line in mfile:
#             linesp = line.split(",")
#             term1 = linesp[0]
#             term2 = linesp[1]
#             print(term1, term2)
#             def1 = ud.define(linesp[0])
#             def2 = ud.define(linesp[1])
#             l1 = []
#             l2 = []
#             for d in def1:
#                 like1 = d.upvotes
#                 l1.append(like1)
#             for d in def2:
#                 like2 = d.upvotes
#
#                 l2.append(like2)
#             print(l1,l2)
#     print('n')
#     dt = datetime.now() + timedelta(hours=1)
#     dt = dt.replace(minute=1)
#     while datetime.now() < dt:
#         datetime(2017,8,25)
sched = BlockingScheduler()
@sched.scheduled_job('interval',hours=1)
def timed_job():
    with open("mc_wordpair.csv", "r") as mfile:
        for line in mfile:
            linesp = line.split(",")
            def1 = ud.define(linesp[0])
            def2 = ud.define(linesp[1])
            l1 = []
            l2 = []
            sentence1 = []
            sentence2 = []
            for d in def1:
                like1 = d.upvotes
                l1.append(like1)
            for d in def2:
                like2 = d.upvotes
                l2.append(like2)

            if len(l1) != 0:
                if len(l2) != 0:
                    maxl1 = max(l1)
                    maxl2 = max(l2)
                    s1 = []
                    s2 = []
                    upv1 = []
                    down1 = []
                    upv2 = []
                    down2 = []
                    for p in def1:
                        s = p.definition
                        u = p.upvotes
                        d = p.downvotes
                        s1.append(s)
                        upv1.append(u)
                        down1.append(d)
                    for q in def2:
                        ss = q.definition
                        uu = q.upvotes
                        dd = q.downvotes
                        s2.append(ss)
                        upv2.append(uu)
                        down2.append(dd)

                    r1 = []
                    r2 = []

                    for j in range(len(s1)):
                        sen1 = s1[j]
                        if down1[j] & upv1[j] <= 0:
                            r = 0
                        else:
                            r = upv1[j] / upv1[j] + down1[j]
                        r1.append(r)
                    max1 = max(r1)
                    for k in range(len(s2)):
                        sen2 = s2[k]
                        if down2[k] & upv2[k] <= 0:
                            r = 0
                        else:
                            r = upv2[k] / (upv2[k] + down2[k])
                        r2.append(r)
                    max2 = max(r2)
                    for d1 in range(len(s1)):
                        if r1[d1] == max1:
                            n = s1[d1]
                            sentence1.append(n)
                    for d2 in range(len(s2)):
                        if r2[d2] == max2:
                            m = s2[d2]
                            sentence2.append(m)

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
            for d1 in range(len(sentence1)):
                ss1 = sentence1[d1]
                ss2 = sentence2[d1]
                sim1 = cos_similarity(ss1, ss2)
                sim2 = cos_similarity(ss2, ss1)
                sim = (sim1 + sim2) / 2.0
                print(sim)
    print('This job is run every 1 hour.')
sched.start()