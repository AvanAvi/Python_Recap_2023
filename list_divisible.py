my_list= [11, 20, 123, 40, 50]

number = int(input("enter a number bw 01 and 99: "))

for i in my_list:
    if i % number ==0:
        print(i,end=" ")

        
    