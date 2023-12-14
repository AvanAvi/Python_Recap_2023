nums = [12,23.23,4560,242,112,1,43.-12,20]



for i in range (0,len(nums)):
    if nums[i] %2 ==0 and nums[i] %5 ==0:
        print(nums[i],end=" ")
    else :
        print("not found",end=" ")
        


