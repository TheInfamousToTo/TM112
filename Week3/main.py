#test
print ("hello ALL " )
#int marks, mark1, mark2, mark3 

mark1=eval(input("enter your TMA marks :"))
mark2=eval(input("enter your MID marks :"))
mark3=eval(input("enter your final mark marks :"))
print ("===================================================")
print("your TMA mark is : ", mark1)
print("your MID mark is : ", mark2)
print("your FINAL mark is : ", mark3)
marks=int(mark1+mark2+mark3)
print("your total mark is : ", marks)
if marks >=50 and marks<=100:
    print("PASS")
elif marks >=0 and marks<=50:
    print
else :
    pri