class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        step = 0
        sum_ = 0
        min_length = len(nums) + 1  # Initialize to a value larger than any possible subarray length
        
        for i in range(len(nums)):
            sum_ += nums[i]  # Add current element to the sum

            # Shrink the window when the sum is >= target
            while sum_ >= target:
                min_length = min(min_length, i - step + 1)
                sum_ -= nums[step]  
                step += 1  # Move the left pointer forward
        
        # Return the result: if no valid subarray was found, return 0
        return min_length if min_length <= len(nums) else 0

#Input: target = 7, nums = [2,3,1,2,4,3] #Output: 2  ([4,3])
#Input: target = 4, nums = [1,4,4] #Output: 1  ([4])
