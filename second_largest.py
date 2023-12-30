list =[12,123,836,832,62,81,817,52,71,62,71,71]

largest = list[0]
second_largest = None

for i in list:
    if i > largest:
        second_largest = largest
        largest = i
    elif second_largest is None or i > second_largest:
        second_largest = i


print(second_largest)