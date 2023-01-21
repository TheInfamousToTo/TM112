#!/usr/bin/env python3

""" Data analysis program 18
"""

# 22/02/2017

from table_utils import *
from stats_utils import * # For correlation calculation

# Load datasets
geog_table = load('geog_2.txt')
mort_table = load('mort_1.txt')

# Create empty lists
mort_list = []
geog_list = []

for mort_row in mort_table:
    area = mort_row[0]
    for geog_row in geog_table:
        if area == geog_row[1]: # Is area name in both lists?
             mort_list.append(float(mort_row[1]))
             geog_list.append(float(geog_row[2])) 

corr = round(corr_coef(mort_list, geog_list), 2)
print('Correlation coefficient =', corr)


