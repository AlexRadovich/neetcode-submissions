class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minn = prices[0]
        maxx = prices[0]
        poten = 0
        for i in range(len(prices)):
            if prices[i] < minn:
                minn = prices[i]
                maxx = prices[i]
            elif prices[i] > maxx:
                maxx = prices[i]
                poten = max(poten,maxx - minn)
        return poten
            