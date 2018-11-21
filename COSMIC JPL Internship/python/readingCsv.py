import csv

with open ('fresh-impact-pre-filter-classifications-2018-02-07.csv') as csvfile
	readCSV = csv.reader(csvfile, delimiter=',')

	for row in readCSV:
		print(row)