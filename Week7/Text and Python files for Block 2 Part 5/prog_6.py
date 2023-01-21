#!/usr/bin/env python3

""" Data analysis program 6
"""

# 06/02/2017

import csv

file = open('happ_1.txt', 'r')
table =[]
reader = csv.reader(file)
for row in reader:
    table.append(row)

from table_utils import *

table2 = rows(table, 1, 11)
table3 = cols(table2, 1, 4)
table4 = flip(table3)
table5 = to_float(table4)
print(table5)





