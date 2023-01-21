#!/usr/bin/env python3

"""
Utilities for processing tables (list of lists)
"""

# 19/02/2016

import csv
import re


def rows(table, start, stop):
    """ Return rows of table between
start (inclusive) and stop (inclusive).

"""

    return table[start : stop + 1]



def cols(table, start, stop):
    """ Return columns of table between
start (inclusive) and stop (inclusive).

"""

    return [list1[start : stop + 1] for list1 in table]



def flip(table):
    """ Return result of swapping the rows and columns of table.

"""

    return [list(tuple1) for tuple1 in list(zip(*table))]



def to_float(table):
    """ Returns a new table with entries converted to
floats where possible, otherwise left unchanged.

"""
    table1 = []
    for row in table:
        row1 = []
        for item in row:
            try:
                row1.append(float(item))
            except ValueError:
                row1.append(item)
        table1.append(row1)
    return table1
 
    
    
def filter_by(string, column, table):
    """ Return rows of table for which the value in column starts
with string. Accepts period . as wildcard character.

"""

    return [row for row in table if re.match(string, row[column])]


def sort_by(column, table):
    """ Return a new table with rows sorted on the values in column.
"""
    
    return sorted(table, key = lambda row: row[column])



def save(table, filename):
    """ Save table data to file as csv.

"""

    with open(filename, 'wt', encoding='iso-8859-1') as outfile:
        csv.writer(outfile).writerows(table)
             


def load(filename):
    """ Load csv data from file and return it as table.

"""

    with open(filename, 'rt', encoding='iso-8859-1') as infile:
        return [row for row in csv.reader(infile)]
