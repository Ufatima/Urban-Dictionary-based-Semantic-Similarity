import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
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
#print(df1.head()) #print csv file with header
#corr = df1.corr()
#print(corr)
#np.savetxt('rg_correlation_matrix.csv', corr, '%0.12f')

x = df1.hu_ju
y = df1.wup
r1 = pearson_correlation(x, y)
print(r1)
