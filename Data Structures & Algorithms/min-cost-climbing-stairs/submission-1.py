class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        memo = [0] * (len(cost))



        for ix, n in enumerate(cost):
            if ix == 0 or ix == 1:
                memo[ix] = n
                continue
            
            memo[ix] = min(memo[ix-2],memo[ix-1]) + n

        return min(memo[-1],memo[-2])
            
            