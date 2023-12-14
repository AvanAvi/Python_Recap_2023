import time
def sort(nums):
    for i in range (len(nums)-1,0,-1):
        for j in range (i):
            if nums[j]> nums[j+1]:
                temp = nums[j]
                nums[j]= nums[j+1]
                nums [j+1] = temp

        








nums = [51, 85, 1748, 52, 44, 100, 200]
sort(nums)


start_time = time.time()
sort(nums)
end_time = time.time()


print(nums,end=" ")
print(end_time-start_time)
                            