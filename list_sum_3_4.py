x= [51,85,1748,52,44,100,200]
total =0
for i in range (0,len(x)):
    if x[i]%3 ==0 or x[i]%4 == 0:
        total = total +x[i]
        print(total,end=" ")
