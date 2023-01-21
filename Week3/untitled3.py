temp=eval(input("enter the temperature :"))
unit=input("enter the unit (F OR C ) :")
if unit=='F':
    output = ((9*temp) / 5)
    print ("the temperature in Celsius is :", output)
elif unit=='C':
    output = (5/9*(temp-32))
    print ("the temperature in Fahrenheit is :", output)
else :
    print ("Wrong input")