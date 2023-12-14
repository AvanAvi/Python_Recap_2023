x = [51, 85, 1748, 52, 44, 100, 200]

count_positive = 0
count_negative = 0

for i in range(0, len(x)):
    if x[i] > 0:
        count_positive = count_positive + 1
       

    elif x[i] < 0:
        count_negative = count_negative + 1
       
        
print("the total number of +ive integers is : ", count_positive)
print("the total number of -ive integers is : ", count_negative)

     