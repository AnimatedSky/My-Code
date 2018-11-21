import matplotlib.pyplot as plt
import numpy as np
import csv

with open('mars-class2 .csv' 'r') as FreshImpacts:
	csv_reader = csv.reader(FreshImpacts)
	header = csvReader.next()
	