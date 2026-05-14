class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0,len(heights)-1

        maxx = -1
        while(l<r):
            amount = (r-l) * min(heights[r],heights[l])
            print(amount)
            maxx = max(maxx,amount)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxx