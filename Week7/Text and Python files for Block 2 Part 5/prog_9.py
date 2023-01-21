""" Data analysis program 9
"""

# 14/02/2017

def median(alist):
    """ Calculates the median of a list of numbers.
The list must not be empty.
"""

    number_of_values = len(alist)
    sorted_list = sorted(alist)

    # Two cases, depending on whether the number of values is odd or even.
    quotient = number_of_values // 2
    remainder = number_of_values % 2
 
    if (remainder == 1):
        result = sorted_list[quotient]
    else:
        result = (sorted_list[quotient - 1] + sorted_list[quotient]) / 2
    return result
        
    
def test_median():
    assert median([2]) == 2
    assert median([4, 3]) == 3.5
    assert median([3, 1, 8, 4, 7, 6, 4, 2, 5, 9]) == 4.5
    assert median([7, 2, 6, 2, 5, 3, 1, 0, 8, 6, 6, 4, 9]) == 5

test_median()


    
