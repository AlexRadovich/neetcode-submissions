class Solution:
    def climbStairs(self, n: int) -> int:
        sum = 0
        def fib(k):
            if k==1: return 1
            if k==2: return 2
            
            return fib(k-1) + fib(k-2)
        sum = fib(n)
        return sum