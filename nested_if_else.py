num1 = int(input("enter the 1st number  "))
num2 = int(input("enter the  2nd number  "))
num3 = int(input("enter the 3rd number  "))

if num1 > num2:
    if num1 > num3:
        print("num1 is the greatest")
    else:
        print("num3 is the greatest")
else:
    if num2 > num3:
        print("num2 is the greatest")
    else:
        print("num3 is the greatest")