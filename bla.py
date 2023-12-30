def common(list_1,list_2):
    list_3= []
    for i in list_1:
        if i in list_2:
            list_3.append(i)
    return list_3     


list_1 = [11, 20, 123, 17, 5,12,13]
list_2 = [11, 200, 1223, 17, 15,12,13]

print(common(list_1,list_2))