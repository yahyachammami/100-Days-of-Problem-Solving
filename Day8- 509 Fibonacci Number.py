class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Base cases
        if n == 0:
            return 0
        elif n == 1:
            return 1

        return self.fib(n - 1) + self.fib(n - 2)
    
""" Fibonacci sequence, such that each number is the sum of the two preceding ones"""