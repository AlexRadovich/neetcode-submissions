class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0,len(nums) - 1

        while r-l > 1:
            if(nums[l]<nums[r]): return nums[l]
            print(l,r)
            m = (r+l)//2
            if nums[m] > nums[l]:
                l = m
            else:
                r = m
            
        return min(nums[l],nums[r])
