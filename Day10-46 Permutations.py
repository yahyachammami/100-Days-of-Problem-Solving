class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 1:
            return [nums]  

        l = []  
        for i in range(len(nums)):
            remaining = nums[:i] + nums[i+1:]
            for perm in self.permute(remaining):
                l.append([nums[i]] + perm)
        
        return l

sol = Solution()
print(sol.permute([1, 2, 3]))
[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
