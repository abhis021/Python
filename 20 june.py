#w='python'
#print(w[1])
#print(w[-1])
#print([])

#p=[1, 2, 3]
#print(p.append(4))
#print(p.insert(1, "joey"))
#print(p.pop())

#n=input("Enter your name bro:")
#print("So you are "+n+"."+"\nConfirm that you are "+ n )
#print("Yes or NO")
#x=input("")
#if("y" in x):
#    print("Oh so you really are " +n)
#else:
#    print("Oh so you are not "+n)
#print("HELLO Player!")

#a=int(input("How Many Round You Want To Roll The Dice? "))

#b=0

#c=0

#import random
#for i in range(0,a):
#    d=random.randrange(1,6)
    
#e=random.randrange(1,6)
#while d==e:
#    b+=d
#    print("Your score is:",b)
#c+=e
#print("My Score is:",c)
#print("Your Score",b)
#print("My Score",c)
#if b>c:
#        print("You Won")
#else:
#    print("You Lose")

import random
min = 1
max = 6

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    print("Rolling the dices...")
    print("The values are....")
    print(random.randint(min, max))
    print(random.randint(min, max))

    roll_again = input("Roll the dices again?")
