class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        k = nums[0]

        for i in range(1,len(nums)):
            k ^= nums[i]

        return k
        