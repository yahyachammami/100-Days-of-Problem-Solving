class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set() # Set to Track Seen Numbers
        
        while n != 1 and n not in seen:
            seen.add(n) # prevents infinite loops
            n = sum(int(digit)**2 for digit in str(n))
        
        return n == 1

#solution = Solution()
#print(solution.isHappy(19))  # Output: True (19 is a happy number)
#Explanation: 12 + 92 = 82 , 82 + 22 = 68 , 62 + 82 = 100 , 12 + 02 + 02 = 1

