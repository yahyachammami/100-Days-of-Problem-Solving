class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0:
            return 0  # k cannot be negative
        
        seen = set()
        unique_pairs = set()
        
        for num in nums:
            if num + k in seen:
                unique_pairs.add((num, num + k))
            if num - k in seen:
                unique_pairs.add((num - k, num))
            seen.add(num)
        
        return len(unique_pairs)



solution = Solution()
print(solution.findPairs(nums, k))  
# Input nums = [3, 1, 4, 1, 5] k = 2 # Output: 2