class Solution(object):
    def predictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        pick_hisory = {}

        def calculate_score(start, end):
            if start == end: 
                return nums[start]

            pick_start = nums[start] - calculate_score(start + 1, end)
            pick_end = nums[end] - calculate_score(start, end - 1)

            pick_hisory[(start, end)] = max(pick_start, pick_end)

            if (start, end) in pick_hisory:
                return pick_hisory[(start, end)]

            return pick_hisory[(start, end)]

        return calculate_score(0, len(nums) - 1) >= 0

# nums = [1, 5, 2]

# calculate_score(1, 2) = 3 (from choices 5 - 2 and 2 - 5)
# calculate_score(0, 1) = 4 (from choices 1 - 5 and 5 - 1)
# calculate_score(0, 2) = -2 (from choices 1 - 3 and 2 - 4)
# calculate_score(2, 2) = 2  calculate_score(1, 1) = 5  calculate_score(0, 0) = 1

# memo = {(2, 2): 2, (1, 1): 5, (1, 2): 3, (0, 0): 1, (0, 1): 4, (0, 2): -2}
# -2<0 ------> player2 win 