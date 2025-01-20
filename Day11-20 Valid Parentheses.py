class Solution(object):
    def isValid(self, s):
        dict = {')': '(', '}': '{', ']': '[',}
        stack = []

        for char in s :
            if char in dict:
                if stack and stack[-1]==dict[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return len(stack)==0
            

## Input: s = "()[]{}" Output: true
## Input: s = "(]" Output: false

