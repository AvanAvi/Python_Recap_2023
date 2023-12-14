list_1 = [11, 20, 123, 40, 50]
list_2 = [111, 201, 1123, 410, 510]

list_3=[]

for i in  list_1:
    list_3.append(i)
    print("list_3 after step 1 is ", list_3)

for j in list_2:

    list_3.append(j)
    print("list_3 after step 2 is ", list_3)


print("list_3 is ", list_3)