list_1 = [11, 20, 123, 40, 50]
list_2 = [111, 20, 123, 410, 510]


list_3=[]

for i in list_1:
    if i in list_2:
        list_3.append(i)

print("Common elements are :",list_3)

print(list_3, end=" ")        