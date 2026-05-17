class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        m = 0

        if nums[l] == target: return l
        if nums[r] == target: return r

        while ( nums[m] != target):
            m = (l+r)//2

            

            if nums[m] < target:
                if l == m: return -1
                l = m
            else:
                if r == m: return -1
                r = m

        if nums[m] == target: return m

        return -1
