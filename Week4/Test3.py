import random
upper_limit2 = 12
lower_limit2 = 0
size=random.randint(lower_limit2, upper_limit2)
print ("size is : " , size)
for row in range(1, size+1):
    for column in range(1, size+1):
        print (row*column , end=' ')
        #print(row*column, end=' ')
    # Move to a new line
    print() 
