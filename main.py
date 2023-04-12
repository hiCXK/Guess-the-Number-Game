from random import *
a=None
name=input("Please enter your name: ")
print("Hello " + name + "!\nI have chosen a number[1,100]...can you guess it?")
x=int(input("Enter your number here: "))
y=randint(1,100)
def getnum():
    x=int(input("Try again: "))
    compare(x,y)
def compare(x,y):
    if (y==x):
        print("YES! You got that right.")
        a=input("Play again? Y/N: ") 
        if a=="Y":
            y=randint(1,100)
            getnum()
        if a=="N":
            print("Have a great day " + name + "! Until next time...")
    elif(y>x):
        print("low")
        getnum()
    else:
        print("high")
        getnum()
        
           
getnum() 