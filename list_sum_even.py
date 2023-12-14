x= [12,35,64,85,83,90,24,36,42,65,70]

total=0

for i in range (0,len(x)):
    if x[i] %2 ==0:
        total=total+x[i]

print(total)
