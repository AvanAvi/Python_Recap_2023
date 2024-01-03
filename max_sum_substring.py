def max_sum_increasing_subseq(arr):
    """
    Function to find the maximum sum of increasing subsequence in an array.
    
    :param arr: List of integers
    :return: Maximum sum of the increasing subsequence
    """
    
    # Length of the array
    n = len(arr)
    
    # max_sum[i] will store the maximum sum of increasing subsequence
    # ending with arr[i]
    max_sum = arr.copy()  # Initially, the max sum is same as the array elements
    
    # Compute the maximum sum values in bottom up manner
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and max_sum[i] < max_sum[j] + arr[i]:
                max_sum[i] = max_sum[j] + arr[i]
                
    # Return maximum value in max_sum[]
    return max(max_sum)

# Example array
arr = [10, 5, 4, 3, 2, 1, 100]

# Find the maximum sum increasing subsequence
max_sum = max_sum_increasing_subseq(arr)
max_sum
