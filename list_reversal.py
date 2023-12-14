# Create a sample list
my_list = [10, 21, 32, 43, 54, 65, 76, 87, 98, 109]

# Iterate over the list and print elements at even indices
for i in range(len(my_list)):
    if i % 2 == 1:
        print(my_list, end=" ")
