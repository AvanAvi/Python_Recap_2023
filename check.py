def add(n1,n2):
    total = n1+n2
    return total

def check(num):
    if num % 2 == 0:
        print("even")
    
    else:        
        print("odd")

x = int(input("enter the first number : "))
y = int(input("enter the second number : "))

sum = add(x,y)
check(sum)


