a= input("enter the email ")
print("@" in "Contains" +a)

string=input("Enter your name")
print(string.isupper())



string ='Hello Alien'

newstring =''
count1 = 0

count2 = 0

count3 = 0
  

for a in string:
    if (a.isupper()) == True: 

        count1+= 1

        newstring+=(a.lower())
   elif (a.islower()) == True:
        count2+=1
        newstring+=(a.upper()) 
 

    elif (a.isspace()) == True:
        count3+= 1
      newstring+= a 

print("In original String : ") 

print("Uppercase -", count1) 

print("Lowercase -", count2) 

print("Spaces -", count3) 
  


print("After changing cases:")
print(newstring) 

