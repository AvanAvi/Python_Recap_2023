my_list =[]

for i in range (10):
    number = int (input(f"enter the number {i}:  "))
    my_list.append(i)
print(my_list)

result=[]   
for j in range(len(my_list)-1,-1,-1):
    result.append(my_list[j])

print(result)

