list = [1, 2, 3, 4, 5,7,22]

first_element= list[0]
last_element= list[-1]

for i in range(0,len(list)):
    if i == 0:
        list[i]= last_element
    elif i == len(list)-1:
        list[i]= first_element
    else:
        list[i] == list[i]

print(list)
