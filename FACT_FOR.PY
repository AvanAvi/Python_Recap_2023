num = int (input("enter the number "))

fact = 1

for num in range (1,num+1):
    fact *= num
    num -= 1
print(fact)
