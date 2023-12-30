list1 =[12,23,-88,73,92,912,921]
list2 =[123,23,-88,73,9211,9212,921]


list3=[]

for i in list1:
    if i in list2:
        list3.append(i)
print(list3)