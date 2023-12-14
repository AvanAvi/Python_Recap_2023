list_1 = [11, 20, 123, 17, 5,12,13,19,19]

list_2=[]

for i in list_1:
    if i in list_2:
        list_1.remove(i)
    else:

        list_2.append(i)


print(list_2, end=" ")      

list_2.reverse()
print(list_2)

    


