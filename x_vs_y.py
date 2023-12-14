x = int(input("enter the number x "))
y = int(input("enter the number y "))

if x<y:
    while (x<=y):
        print(x,end=" ")
        x=x+1

elif y<x:
    while(y<=x):
        print(y,end=" ")
        y=y+1
        