from numpy import genfromtxt
import numpy as np
import time

features = np.genfromtxt("test_data2.csv", delimiter=",", names=True)

#Print the whole nd-array
print(features)

# #Print the names of the columns
# print(features.dtype.names)

# #Print just the column with the name Col2
# print(features["Col2"])

time.sleep(10)