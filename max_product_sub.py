def MaxProduct(nums):
    if not nums :
        return 0
    
    current_product = nums[0]
    max_product = nums[0]
    min_product=nums[0]


    for i in nums[1:]:
        if i == 0:
            current_product = 1
            continue

        temp = current_product*i
        current_product = max(i,temp,min_product*i)
        max_product = max(max_product,current_product)

    return max_product  








print(MaxProduct([-5, -8, 2, 0, 9, 0, 3, -10]))