#!/usr/bin/env python3

""" Data analysis program 17
"""

# 10/03/2017

from table_utils import *
from stats_utils import * # For correlation calculation

""" Add code here to implement the algorithm below (see Activity 20).

load mort_1.txt and geog_2.txt into tables mort_table and geog_table 
create empty lists mort_list and geog_list
for mort_row in mort_table
    set area to mort_row[0]
    for geog_row in geog_table
        if area == geog_row[1]
            append float(mort_row[1]) to mort_list
            append float(geog_row[2]) to geog_list    
"""

corr = round(corr_coef(mort_list, geog_list), 2)
print('Correlation coefficient =', corr)

