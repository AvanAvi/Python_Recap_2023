def quicksort(nums, left, right):
    if left < right:
        partition_pos = partition(nums, left, right)
        quicksort(nums, left, partition_pos - 1)
        quicksort(nums, partition_pos + 1, right)

def partition(nums, left, right):
    i = left
    j = right - 1
    pivot = nums[right]

    while i < j:
        # Increment i until we find a value greater than the pivot
        while i < right and nums[i] < pivot:
            i += 1
        # Decrement j until we find a value less than the pivot
        while j > left and nums[j] >= pivot:
            j -= 1
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]

    # Swap the pivot into its correct position
    if nums[i] > pivot:
        nums[i], nums[right] = nums[right], nums[i]
    return i

nums = [12, 136, 71, 72, 82, 92, 362, -3, 93, 63, 0, -32]
quicksort(nums, 0, len(nums) - 1)
print(nums)
