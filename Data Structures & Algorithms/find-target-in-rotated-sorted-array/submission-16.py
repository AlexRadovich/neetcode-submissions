class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums: return -1
        if len(nums) == 1 and nums[0] == target: return 0
        if len(nums) == 1: return -1
            

        l,r = 0, len(nums)-1

        found = False
        ct = 0

        if nums[l] < nums[r]:
            low, high = l,r
        else:
            m = 0

            while  l < r and ct < 10:
                ct += 1
                m = (l+r)//2

                if nums[m] < nums[l] :
                    if r == m:
                        break
                    r = m
                elif nums[m] > nums[r]:
                    if l == m:
                        break
                    l = m

            low, high = m+1, m
        

        if nums[0] <= target <= nums[high]:
            l = 0
            r = high

        elif nums[low] <= target <= nums[-1]:
            l = low
            r = len(nums)-1

        else:
            return -1
        
        print(l,r)

        if nums[l] == target: return l
        if nums[r] == target: return r

        while(1):

            m = (l+r)//2

            if nums[m] == target: return m

            elif m < target:
                if l == m:
                    return -1
                l = m
            else:
                if r == m:
                    return -1
                r = m
                





            
        