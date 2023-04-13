from random import *
a=None

c=1


name=input("Please enter your name: ")
print("Hello " + name + "!\nI have chosen a number[1,100]...can you guess it?")

def getnum():
    x=int(input("Try again: "))
    compare(x,y)

def getnum2():
    global y
    y=randint(1,100)
    x=int(input("Enter your number: "))
    compare(x,y)
def compare(x,y):
    if (y==x):
        print("YES! You got that right!")
        a=input("Play again? Y/N: ") 
        if a=="Y":
            print("I have again chosen a number[1,100]. Find it!")
            y=randint(1,100)
            getnum2()
        if a=="N":
            print("Have a great day " + name + "! Until next time...")
    elif(y>x):
        print("It is low")
        getnum()
    else:
        print("It is high")
        getnum()
        
           
getnum2() 