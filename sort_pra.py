import time
def sort(nums):
    for i in range (len(nums)-1,0,-1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                temp = nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=temp




nums = [15,82,81,123,75,9392,929,12,]      
sort(nums)

start_time = time.time()
sort(nums)
end_time = time.time()

print(nums,end=" ")
print(end_time-start_time)

