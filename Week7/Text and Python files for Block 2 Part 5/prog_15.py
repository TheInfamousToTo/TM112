#!/usr/bin/env python3

"""
Data analysis program 15.

Finds UK area where average happiness was highest according to ONS statistics
April 2014 - March 2015.

TM112 Module Team 19/04/2017

"""

# 10/03/2017

from table_utils import *

# Load geog_1.txt data into table0
table0 = load('geog_1.txt')

""" Overall strategy is to process Scotland separately from the
other countries because its authority codes start differently. """

""" STAGE 1: process data for Wales, Northern Ireland and England. """

# Filter selects all authorities in Wales, Northern Ireland and England.
# These all have codes beginning with '.0'.
table1 = filter_by('.0', 0, table0)

# Filter removes rows where column 7 holds non-numerical data.
table2 = []
for row in table1:
    if row[7] != 'x' and row[7] != '#':
        table2.append(row)

# Convert numerical strings to actual number.
table3 = to_float(table2)

# Sort on column 7, percentage in 'Very High' category.
table4 = sort_by(7, table3)

# Sorting was from lowest to highest, so now we want the last row.
size4 = len(table4)
table4_best = table4[size4 - 1]

""" STAGE 2: process data for Scotland. """

# Filter selects all authorities in Scotland.
# These all have codes beginning with '12'.
table5 = filter_by('S12', 0, table0)

# Follow same steps as before to filter and sort.
table6 = []
for row in table5:
    if row[7] != 'x' and row[7] != '#':
        table6.append(row)

table7 = to_float(table6)

table8 = sort_by(7, table7)

# Find last row
size8 = len(table8)
table8_best = table8[size8 - 1]

""" STAGE 3: compare two best authorities to find overall winner. """
if table4_best[7] > table8_best[7]:
    winner = table4_best
else:
    winner = table8_best

# Print winner
print('The authority with the most people in the Very High category was', winner[3])
print('The percentage in the Very High category was', winner[7])
