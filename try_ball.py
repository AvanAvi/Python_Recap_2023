def MaxProduct(nums):
    if not nums :
        return 0
    
    current_max = current_min = max_product = nums[0]

    for i in nums[1:]:
        if i ==0 :
            current_max = current_min = 1
            max_product= max(max_product,0)
            continue


        temp = current_max*i
        current_max=max(i,temp,current_min*i)
        current_min=min(i,temp,current_min*i) 
        max_product=max(current_max,max_product)

    return max_product

print(MaxProduct([2,3,-2,4]))  
print(MaxProduct([-2,0,-1]))









    