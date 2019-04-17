import gensim
from nltk.corpus import stopwords
import numpy as np
stop = set(stopwords.words('english'))
model = gensim.models.KeyedVectors.load_word2vec_format('./models/GoogleNews-vectors-negative300.bin', binary=True)
word = 'car'
sets = model.most_similar(word, topn = 10)
print(sets)
