list =[12,123,836,832,62,81,817,52,71,62,71,71]

product = 1

for i in list:
    product= product *i
    i=i+1
print(product)
print(id(product))