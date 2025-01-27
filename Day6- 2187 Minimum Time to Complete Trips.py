class Solution1(object):
    def minimumTime(self, time, totalTrips):
        """
        :type time: List[int]
        :type totalTrips: int
        :rtype: int
        """
        t = 1  
        while True:
            trips = 0  
            for bus_time in time:
                trips = trips + (t // bus_time)  

            if trips >= totalTrips:
                return t

            t = t + 1
            

## Two-Pointer Approach

class Solution2(object):
    def minimumTime(self, time, totalTrips):
        
        # Binary search bounds
        left, right = 1, max(time) * totalTrips
        
        # Binary search loop
        while left < right:
            mid = (left + right) // 2
            total = 0
            
            # Calculate total trips completed by all buses at time 'mid'
            for t in time:
                total += mid // t
            
            # Check if we can complete the required totalTrips
            if total >= totalTrips:
                right = mid  # Try to reduce the time
            else:
                left = mid + 1  # Increase the time
        
        return left
