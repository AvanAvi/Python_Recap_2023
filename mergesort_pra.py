def merge(left,right):
    result=[]
    i,j= 0,0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i= i+1

        else:
            result.append(right[j])
            j= j+1

    result+=left[i:]
    result+=right[j:]
    return result

def merge_sort(nums):
    if len(nums)<=1:
      return nums

    mid=len(nums)//2
    left=merge_sort(nums[:mid])
    right=merge_sort(nums[mid:])
    return merge(left,right)

        
nums = [12,136,71,72,82,92,362,-3,93,63,0,-32]
print(merge_sort(nums))
