#!/usr/bin/env python3

""" Data analysis program 8
"""

# 06/02/2017

import csv

file = open('happ_1.txt', 'r')
table = []
reader = csv.reader(file)
for row in reader:
    table.append(row)

from table_utils import *

table2 = rows(table, 1, 11)
table3 = cols(table2, 1, 4)
table4 = flip(table3)
table5 = to_float(table4)
print(table5)

for row in table5:
   numbers = row
   total = 0
   for rating in range(11):
      product = rating * numbers[rating]
      total = total + product
   average = total / 100
   print('average rating =', round(average, 1))



