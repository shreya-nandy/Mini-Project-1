'''
1=snake
0=gun
-1=water
'''

import random
computer=random.choice([1,0,-1]) # to choose a number randomly from the list
you_str=input("Enter your choice between s/S for Snake ,g/G for Gun and w/W for Water): ")
youDict={"s":1,"g":0,"w":-1,"S":1,"G":0,"W":-1}

you=youDict[you_str]

reverseDict={1:"Snake",0:"Gun",-1:"Water"}

print(f"You chose {reverseDict[you]} AND Computer chose {reverseDict[computer]}")

if(computer==you):
    print("It's a draw")
    
else:
    if(computer==-1 and you==1):
        print("You Won!")
    elif(computer==-1 and you==0):
        print("You Lose!")
    elif(computer==1 and you==-1):
        print("You Lose!")
    elif(computer==1 and you==0):
        print("You Won!")
    elif(computer==0 and you==-1):
        print("You Won!")
    elif(computer==-0 and you==1):
        print("You lose!")
    else:
        print("Please a valid input here (Snake / Gun / Water)")