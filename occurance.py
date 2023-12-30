list =[12,123,836,832,62,81,817,52,71,62,71,71]
max_count=0
max_element=None

for i in list:
    count=list.count(i)
    if count > max_count:
        max_count=count
        max_element=i
print(max_element)
print(max_count)

      
