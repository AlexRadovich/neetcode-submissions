class Solution:
    def jump(self, nums: List[int]) -> int:
        
        ix = 0
        ct = 0

        while ix < len(nums)-1:
            print("IX",ix)
            best = -1
            bix = ix
            decay = 0
            for i in range(ix+1,ix+nums[ix]+1):
                if i >= len(nums)-1:
                    return ct +1
                if decay + nums[i] >= best:
                    best = decay + nums[i]
                    print("B",best)
                    bix = i
                decay += 1
            ix = bix
            ct += 1
            print("JUMPED")
        print(ix)

        return ct