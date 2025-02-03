class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        step = 0
        min_len = len(nums)+ 1
        sum_ = 0

        for i in range(len(nums)):
            sum_ += nums[i]

            while sum_ >= target :
                min_len = min(min_len, i-step+1)
                sum_ -= nums[step] 
                step += 1
        return min_len if min_len <= len(nums) else 0  

#Input: target = 7, nums = [2,3,1,2,4,3] #Output: 2  ([4,3])
#Input: target = 4, nums = [1,4,4] #Output: 1  ([4])
