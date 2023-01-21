
def fact1(nn):
    nn=eval(input("Enter N :"))
    if nn==1 : 
        return 1
    else : 
        return nn*fact1(nn-1)
        print("factorial value of ",nn,"=",fact1)