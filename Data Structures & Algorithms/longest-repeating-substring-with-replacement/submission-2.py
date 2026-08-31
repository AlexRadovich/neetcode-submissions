from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s: return 0
        if k >= len(s): return len(s)
        l,r = 0,0

        count = defaultdict(int)
        count[s[r]] += 1

        best = 0

        ct = 0

        while r < len(s):
            #print(l,r)
            slack = (r-l+1) - max(count.values())
            
            if slack <= k and r < len(s)-1:
                best = max(best,r-l+1)
                r += 1
                count[s[r]] += 1
            elif slack > k:
                count[s[l]] -= 1
                l += 1
            elif r ==len(s)-1:
                best = max(best,r-l+1)
                break
            else:
                break
    

        return best


