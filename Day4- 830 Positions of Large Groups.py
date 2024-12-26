class Solution:
    def largeGroupPositions(self, s):
        result = []  
        start = 0  

        for i in range(1, len(s)): 
            if s[i] != s[i - 1]:  
                if i - start >= 3: 
                    result.append([start, i - 1]) 
                start = i  # Reset start index

        if len(s) - start >= 3:  # Check the last group after the loop ends
            result.append([start, len(s) - 1])  # If the last group is large, add the interval to the result list
        
        return result  


sol = Solution()
print(sol.largeGroupPositions("abbxxxxzzy"))  # Output: [[3,6]]
print(sol.largeGroupPositions("abc"))  # Output: []
print(sol.largeGroupPositions("abcdddeeeeaabbbcd"))  # Output: [[3,5],[6,9],[12,14]]
