from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        r = max(piles)
        l = 0


        while l < r:
            print("l and r",l,r)
            steps = 0
            c = piles[:]
            candidate = (l+r)//2
            if candidate == 0 : return 1

            print("cand: ",candidate)

            for i in c:
                steps += ceil(i / candidate)

            # if steps == h:
            #     print("got it")
            #     return candidate
            if steps <= h:
                if r == candidate:
                    print("r")
                    return l
                r = candidate
            elif steps > h:
                if l == candidate:
                    print("l")
                    return r
                l = candidate





