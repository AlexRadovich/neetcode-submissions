class Solution:
    def canJump(self, nums: List[int]) -> bool:
        ix,jump = 0,nums[0]


        def dfs(ix):
            if(ix >= len(nums)-1):
                return True
            if(nums[ix] == 0):
                return False

            for i in range(1,nums[ix]+1):
                if dfs(ix+i):
                    return True
            return False
            
        return dfs(0)

                

        

            
        