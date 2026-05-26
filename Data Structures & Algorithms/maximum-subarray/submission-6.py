class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        
        best = current = float('-inf')

        for i in nums:
            

            if current + i < i:
                current = i
            else:
                current += i



            print(best,current)
            best = max(best,current)

            


        return max(current,best)

        
