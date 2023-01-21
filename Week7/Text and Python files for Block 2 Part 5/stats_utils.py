#!/usr/bin/env python3

# This version 25/03/2016

# Statistical utilities
import math

def mean(list):
    """Return mean of list"""
    sum = 0
    count = 0
    for item in list:
        sum = sum + item
        count = count + 1
    return sum / count

def var(list):
    """ Return variance of list"""
    avg = mean(list)
    sum_deviations = 0
    for item in list:
        sum_deviations = sum_deviations + (item - avg)**2
    return sum_deviations / (len(list) - 1)
    
def test_mean():
    list = [1, 2, 3, 4, 5]
    assert(mean(list) == 3)
    
def test_var():
    list = [1, 2, 3, 4, 5]
    assert(var(list) == 2.5)
    
# Unit tests
test_mean()
test_var()


def corr_coef(list_x, list_y):
    """ Return correlation between values in list_x and list_y.

    Lists must be of equal length.
    
    """
    
    x_bar = mean(list_x)
    y_bar = mean(list_y)
    sxy = 0
    sxx = 0
    syy = 0
    for index in range(len(list_x)):
        x = list_x[index]
        y = list_y[index]
        sxy = sxy + (x - x_bar) * (y - y_bar)
        sxx = sxx + (x - x_bar) * (x - x_bar)
        syy = syy + (y - y_bar) * (y - y_bar)
    return sxy / math.sqrt(sxx * syy)

def test_corr_coef():
    # Data from M140 Unit 9 Example 5
    list1 = [78.9, 75.8, 77.3, 74.2, 78.1, 72.8, 77.6, 77.9]
    list2 = [56.7, 53.1, 56.1, 55.9, 54.1, 48.6, 59.4, 54.0]
    assert round(corr_coef(list1, list2), 2) == 0.64
    
# Unit test
test_corr_coef()

def index_of_median_group(list):
    total = sum(list)
    cum_total = 0
    for index in range(len(list)):
        cum_total = cum_total + list[index]
        if cum_total >= total / 2:
            return index - 1
        
##list_2012 = [1.4, 0.9, 2.2, 2.7, 3.7, 9.4, 8.7, 15.8, 23.5, 15.4, 16.4]
##list_2013 = [1.2, 0.9, 2.0, 2.5, 3.8, 9.3, 8.8, 16.4, 24.2, 15.6, 15.3]
##list_2014 = [1.1, 0.8, 1.9, 2.5, 3.4, 8.5, 8.6, 16.1, 24.6, 16.3, 16.3]
##list_2015 = [1.0, 0.7, 1.6, 2.3, 3.3, 8.5, 8.2, 15.8, 24.4, 17.0, 17.1]

def median_rating(list):
    total = sum(list)
    semi_total = total / 2
    cum_total = 0
    for index in range(len(list)):
        cum_total = cum_total + list[index]
        if cum_total >= semi_total:
           prev = cum_total - list[index]
           median = index - 1 + (semi_total - prev) / (cum_total - prev)
           return median

##print(median_rating(list_2012))
##print(median_rating(list_2013))
##print(median_rating(list_2014))
##print(median_rating(list_2015))
   
  
            
        


    
    
    
