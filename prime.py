my_list= [11,13,20,24,26,6,8,76,71]

prime_list = []

for i in my_list:
    if i>1:
        for j in range(2,i):
            if i%j ==0:
                break
        else:
            prime_list.append(i)

print(prime_list)