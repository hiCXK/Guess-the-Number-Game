from random import randrange


name=input("Please enter your name: ")
x=int(input("Hello " + name + "!\nI have chosen a number[1,100]...can you guess it?\nEnter your number here: "))
def again(x):
    compare(x)
def compare(x):
    y=randrange(1,101)
    if (y==x):
        print("YES! You got that right.")
        return
    elif(y>x):
        print("low")
        again(x)
        return
    elif(y<x):
        print("high")
        again(x)
        return
    return
again(x)    

    

