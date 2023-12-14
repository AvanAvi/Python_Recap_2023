import time

def sort(nums):
    n = len(nums)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]




nums = [51, 85, 1748, 52, 44, 100, 200]
sort(nums)

start_time = time.time()
sort(nums)
end_time = time.time()

print(nums,end=" ")
print(end_time-start_time)
