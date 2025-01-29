class Solution(object):
    def trap(self, height):
        """
        height: List[int] 
        return: int
        """
        if not height:
            return 0

        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        total_water = 0

        while left < right:
            
            if height[left] < height[right]: # The left bar is shorter than the right bar
                
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    total_water += left_max - height[left]
                left += 1
            else: # The right bar is shorter than or equal to the left bar

                if height[right] >= right_max: 
                    right_max = height[right]
                else:
                    total_water += right_max - height[right]
                right -= 1

        return total_water
