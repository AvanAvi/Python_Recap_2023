def list_sum(n):
    total = 0
   
    for i in n:
        total = total +i
    
    return(total)

nums = [2,3,4,57,71,81,982]

print(list_sum(nums))