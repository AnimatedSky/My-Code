import matplotlib.pyplot as plt
import numpy
from scipy import misc



test = plt.imread("test.png")
training = plt.imread("training.png")
trainingL = plt.imread("training-label.png")

print(test.shape)
print(training.shape)
print(trainingL.shape)