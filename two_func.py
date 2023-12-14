def addition(n1,n2):
    total= n1+n2
    return(total)

def check (num):
    if num% 2 ==0:
        print("even")
    else:
        print("odd")

n1 = int(input("enter number 1 = "))
n2 = int(input("enter number 2 = "))
s= addition(n1,n2)
check(s)



