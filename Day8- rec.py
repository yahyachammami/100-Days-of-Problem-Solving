class Solution(object):
    def kthCharacter(self, k):
        """
        :type k: int
        :rtype: str
        """
        l = ['a'] 
        while len(l) < k:
            l2= []
            for i in range(len(l)):
                next_char = chr(ord(l[i]) + 1)
                l2.append(next_char)
            l = l + l2
        return l[k-1] 
    
# Input: k = 5   Output: "b"
# word = "a".  
# "a", word becomes "b"  -----> "ab"
# "ab", word becomes "bc"  ----->  "abbc"
# "abbc", word becomes "bccd"  ----->  "abbcbccd"
