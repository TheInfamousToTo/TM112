#!/usr/bin/env python3

""" Data analysis program 12
"""

# 18/02/2017

from table_utils import *

# Load geog_1.txt data into table0
table0 = load('geog_1.txt')

# Add code below (see Activity 5.27) to eliminate
# from table0 all rows that have x or # in column 8.
# The result should be stored in table1.

table1 = []
for row in table0:
    if row[8] != 'x' and row[8] != '#':
        table1.append(row)
