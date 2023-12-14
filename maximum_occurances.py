my_list=[1, 2,3 ,4,4,4,5,6,7,9,5,3]

max_count = 0
most_common= None

for i in my_list:
    count = my_list.count(i)
    if count> max_count:
        max_count = count
        most_common = i


print(f"the most common number is {most_common} and it occurs {max_count} times")