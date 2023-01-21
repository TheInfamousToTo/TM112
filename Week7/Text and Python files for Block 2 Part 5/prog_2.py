#!/usr/bin/env python3

""" Data analysis program 2
"""

# 06/02/2017

numbers = [9, 27, 26, 19, 12, 7]
total = 0
for rating in range(6):
   product = rating * numbers[rating]
   total = total + product
average = total / 100
print('average rating =', average)





