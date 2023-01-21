def profile():
    name=input("Enter Your name :")
    DOB=eval(input("Enter Your DOB : "))
    age=2022-DOB
    Address=input("Enter your Address:")
    return[name,age,Address]
Data=profile()

print("Name: ",Data[0])
print("Age: ",Data[1])
print("Address: ",Data[2])