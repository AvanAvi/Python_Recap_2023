x= int(input("enter a number x "))
y= int(input("enter a number y "))

if x<y:
    for x in range (x,y+1):
        print (x,end=" ")
        x=x+1
elif y<x:
    for y in range (y,x+1):
        print (y,end=" ")
        y=y+1