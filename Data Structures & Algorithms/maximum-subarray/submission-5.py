class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==1:return nums[0]

        
        best = 0
        best = current = float('-inf')

        for i in nums:
            

            if current + i < i:
                current = i
            else:
                current += i



            print(best,current)
            best = max(best,current)

            


        return max(current,best)

        
