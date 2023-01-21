import factorial_value_with_def as C

fact=1
n=eval(input("Enter n:"))
for i in range (n,1,-1):
    fact=fact*i
print("factorial value of ",n,"=",fact)
