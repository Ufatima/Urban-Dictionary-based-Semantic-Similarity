import urbandictionary as ud
import string
from nltk.corpus import stopwords
import numpy as np
import pandas

stop = set(stopwords.words('english'))

def similarity(ss1, ss2):
	temparray1 = []
	temparray2 = []
	for i_index, i in enumerate(ss1.lower().split()):
		i = i.strip()
		i = i.strip(string.punctuation)
		i = i.replace("'", "")
		if i not in stop:
			temparray1.append(i)
	set1 = set(temparray1)
	for j_index, j in enumerate(ss2.lower().split()):
		j = j.strip()
		j = j.strip(string.punctuation)
		j = j.replace("'", "")
		if j not in stop:
			temparray2.append(j)
	set2 = set(temparray2)
	ovrlp_sen1_sen2 = set(set1).intersection(set2)
	ovrlp_sen1_sen2_number = len(ovrlp_sen1_sen2)
	sent1len = len(set1)
	sent2len = len(set2)
	maxs = max(sent1len, sent2len)
	overlap_number = ovrlp_sen1_sen2_number/maxs
	return overlap_number

m = []
with open ("rg_word.csv", "r") as myfile:
	for line in myfile:
		linesp = line.split(",")
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
				ss1 = sentencesp1[d1]
				ss2 = sentencesp2[d2]
				sim = similarity(ss1, ss2)
				m.append(sim)
		if len(m):
			a = np.max(m)
			print(a)
		else:
			a = 0.0
			print(a)
		m = []