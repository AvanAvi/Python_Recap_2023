def lengthOfLIS(nums):
    """
    Function to find the length of the longest increasing subsequence in an array.
    
    :param nums: List of integers
    :return: Length of the longest strictly increasing subsequence
    """
    
    if not nums:
        return 0

    # dp array initialized to 1 since the min length is 1 (each number is a subsequence of itself)
    dp = [1] * len(nums)
    
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
                
    return max(dp)

# Example 1
nums1 = [10, 9, 2, 5, 3, 7, 101, 18]
length1 = lengthOfLIS(nums1)  # Expected Output: 4

# Example 2
nums2 = [0, 1, 0, 3, 2, 3]
length2 = lengthOfLIS(nums2)  # Expected Output: 4

# Example 3
nums3 = [7, 7, 7, 7, 7, 7, 7]
length3 = lengthOfLIS(nums3)  # Expected Output: 1

(length1, length2, length3)
