class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []



        for i in range(len(nums)-1):
            fir = -nums[i]

            l,r = i+1, len(nums)-1
            while(l<r and (i == 0 or nums[i] != nums[i-1])):
                if(nums[l]+nums[r] == fir):
                    ans.append((-fir,nums[l],nums[r]))
                    l += 1
                    r -= 1
                    while(nums[l] == nums [l-1] and l < r):
                        l += 1
                elif(nums[l]+nums[r] < fir):
                    l += 1
                else:
                    r -= 1
                
        return ans