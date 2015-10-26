# -*- coding: utf-8 -*-
import csv

csv_reader = csv.reader(open("disciplinas.csv", "r"), dialect = "excel", delimiter = ",")

for row in csv_reader:
	for cell in row:
		x = u"%s"%cell
		print x