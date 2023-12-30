list =[]
list2=[]

for i in range (10):
    num= int(input(f"enter the number {i+1}: "))
    list.append(num)
    list2=list.copy()
    list2.reverse()

print(list)    
print(list2)

