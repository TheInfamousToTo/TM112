#!/usr/bin/env python3

""" Data analysis program 4
"""

# 06/02/2017

table = [[9, 27, 26, 19, 12, 7], 
         [4, 21, 30, 25, 18, 2]]

for row in table:
   numbers = row
   total = 0
   for rating in range(6):
      product = rating * numbers[rating]
      total = total + product
   average = total / 100
   print('average rating =', average)






