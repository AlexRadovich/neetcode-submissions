class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0

        maxx = 0
        dictt = {}
        while(r < len(s)):
            if(dictt.get(s[r],0) == 0):
                dictt[s[r]] = 1
                maxx = max(maxx, r-l+1)
                r += 1
            else:
                l += 1
                r = l
                dictt = {}


        return maxx