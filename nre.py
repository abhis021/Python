a=input('Enter your First name ')
if (a.isupper()):
    print(" ")
else:
    print("error please enter your name in UPPER CASE")
    
b=input('Enter your Last Name ')
if (b.islower()):
    print("Hello!"+ a +" "+ b + ".")

else:
    print("error Please enter your name in lower case")
c=int(input("Please enter your valid age:"))
if (c<0):
    print("Invalid Age!! ")
elif(c>70):
    print("Over Aged! ")

d=input("Enter your valid email: ")
if("@" in d):
    print(" ")
if(d.endswith(".com")):
        print(" ")
else:
    print("The email address you have entered is invalid. Please enter a valid email address.")

