class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i = 0  # Pointer for s

        for j in range(len(t)):  # Loop through t
            if i < len(s) and s[i] == t[j]:  # If characters match, move i
                i += 1
        
        return i == len(s)  # If i reaches len(s), s is a subsequence
