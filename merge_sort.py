import time 
def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]
    return result

def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    
    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    return merge(left, right)

nums = [51, 85, 1748, 52, 44, 100, 200]
print(merge_sort(nums))


start_time = time.time()
merge_sort(nums)
end_time = time.time()
print(end_time-start_time,end=" ")

