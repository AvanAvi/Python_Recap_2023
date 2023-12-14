i=20
total =0

for i in range (20,51):
    if i %4 ==0:
        print(i,end=" ")
        total=total+i
        i=i+1
print(total)    