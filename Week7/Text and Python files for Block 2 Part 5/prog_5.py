#!/usr/bin/env python3

""" Data analysis program 5
"""

# 06/02/2017

import csv

file = open('happ_1.txt', 'r')
table =[]
reader = csv.reader(file)
for row in reader:
    table.append(row)
print(table)





