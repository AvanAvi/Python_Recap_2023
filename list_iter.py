'''
list = [12,13,16,27,92]
old = int(input("enter the old number : "))
new= int(input("enter the new number : "))

for i in range(len(list)):
    if list[i] == old:
        list[i] = new
print(list)  
'''

list = [12,13,16,27,92]
new_list=[]

for i in list:
    if i % 2 ==1:
        new_list.append(i)
print(new_list)

