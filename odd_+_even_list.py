my_list= [11, 20, 123, 40, 50,1233,53,12,14,21]

odd_list=[]
even_list=[]

for i in my_list:
    if i %2 ==0:
        even_list.append(i)
    else:
        odd_list.append(i)

print("odd list is: ",odd_list)
print("even list is: ",even_list)    