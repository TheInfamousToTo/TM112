from turtle import *
import random
color('blue', 'red')
upper_limit = 30
lower_limit = 0
upper_limit1 = 180
lower_limit1 = 0
upper_limit2 = 9999
lower_limit2 = 0
q=-110
for i in range (random.randint(lower_limit2, upper_limit2)) :
    for j in range (1,5):
        forward(100)
        right(90)
    pu()
    forward(110)
    goto(q,q)
    pd()
    q=(q+110)
    
done()
