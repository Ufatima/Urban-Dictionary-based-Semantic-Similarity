import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import kendalltau
import matplotlib.pyplot as plt

def pearson_correlation(object1, object2):
    values = range(len(object1))

    # Summation over all attributes for both objects
    sum_object1 = sum([float(object1[i]) for i in values])
    sum_object2 = sum([float(object2[i]) for i in values])

    # Sum the squares
    square_sum1 = sum([pow(object1[i], 2) for i in values])
    square_sum2 = sum([pow(object2[i], 2) for i in values])

    # Add up the products
    product = sum([object1[i] * object2[i] for i in values])

    # Calculate Pearson Correlation score
    numerator = product - (sum_object1 * sum_object2 / len(object1))
    denominator = ((square_sum1 - pow(sum_object1, 2) / len(object1)) * (square_sum2 -
                                                                         pow(sum_object2, 2) / len(object1))) ** 0.5

    # Can"t have division by 0
    if denominator == 0:
        return 0

    result = numerator / denominator
    return result

df1 = pd.read_csv('rgdatasets_finalout.csv')
x = df1.hu_ju
y = df1.popularity
r = pearson_correlation(x, y)
print('pearson correlation', r)

# calculating kendalltau
x1 = df1.r
#print(x1)
myList = df1.popularity
s = sorted(range(len(myList)),key=lambda x:myList[x])
x2 = list(reversed(s))
print('popularity',kendalltau(x1, x2))
#
# cosine = df1.cosine
# sort_cos = sorted(range(len(cosine)),key=lambda x:cosine[x])
# x3 = list(reversed(sort_cos))
# print('cosine', kendalltau(x1, x3))

#scatterplot
# x = df1.hu_ju
# y = df1.cosine
# plt.subplot(221)
# plt.scatter(x,y, c='k')
# plt.xlabel('human judgement rating')
# plt.ylabel('cosine similarity')
#
# x1 = df1.hu_ju
# y1 = df1.popularity
# plt.subplot(222)
# plt.scatter(x1,y1, c='blue')
# plt.xlabel('human judgement rating')
# plt.ylabel('popularity')
#
# x2 = df1.hu_ju
# y2 = df1.overlap
# plt.subplot(223)
# plt.scatter(x2,y2, c='red')
# plt.xlabel('human judgement rating')
# plt.ylabel('overlap similarity')
#
# x3 = df1.hu_ju
# y3 = df1.hatred
# plt.subplot(224)
# plt.scatter(x3,y3, c='green')
# plt.xlabel('human judgement rating')
# plt.ylabel('hatred')
# plt.show()



