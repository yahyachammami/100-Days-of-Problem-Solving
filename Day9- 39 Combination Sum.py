class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []

        def backtrack(remaining, combination, start):
            if remaining == 0:
                # Found a valid combination
                result.append(list(combination))
                return
            elif remaining < 0:
                # Exceeded the target, stop exploring
                return
            
            for i in range(start, len(candidates)):
                # Include the current candidate
                combination.append(candidates[i])
                # Recursively explore with the updated remaining target
                backtrack(remaining - candidates[i], combination, i)
                # Backtrack: remove the last added element
                combination.pop()
        
        
        backtrack(target, [], 0)
        return result


solution = Solution()
print(solution.combinationSum([2, 3, 6, 7], 7))
[[2, 2, 3], [7]]