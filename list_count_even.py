x= [12,35,64,85,83,90,24,36,42,65,70]
count = 0

for i in range (0,len(x)):
    if x[i] %2 ==0:
        count=count+1
print(count)