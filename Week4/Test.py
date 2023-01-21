from turtle import *
import random
color('blue', 'red')
upper_limit = 30
lower_limit = 0
upper_limit1 = 180
lower_limit1 = 0
upper_limit2 = 9999
lower_limit2 = 0
for i in range (random.randint(lower_limit2, upper_limit2)) :
    forward(random.randint(lower_limit, upper_limit))
    left(random.randint(lower_limit1, upper_limit1))
    forward(random.randint(lower_limit, upper_limit))
    right(random.randint(lower_limit1, upper_limit1))
    if abs(pos()) < 1:
        break
done()
