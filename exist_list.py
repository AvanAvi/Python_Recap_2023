my_list=[11, 20, 123, 40, 50, 111, 201, 1123, 410, 510]

number = int(input("enter any number :  "))

if number in my_list:
    print(my_list.index(number))
else:

    print("-1")

