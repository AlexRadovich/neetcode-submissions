class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ""
        letters = set(t)

        finds = [0] * 52
        for i in t:
            if i.lower() == i:
                finds[ord(i) - ord('a')] += 1
            else:
                finds[ord(i) - ord('A') + 26] += 1

        
        
        tee = hash(str(finds))

        best = ""
        window = finds.copy()

        s += " "

        

        l = r = 0
        ct = 0

        while r < len(s) and ct >= 0:
            print(s[l:r+1])

            if max(window) == 0:
                while l < r:
                    if s[l] not in letters:
                        l += 1
                    else:
                        break
                if best == "" or len(s[l:r]) < len(best):

                    best = (s[l:r])
                    print("BEST: ", best)
                if s[l].lower() == s[l]:
                    window[ord(s[l]) - ord('a')] += 1
                else:
                    window[ord(s[l]) - ord('A') + 26] += 1
                l += 1

            
            elif s[r] in letters:
                if s[r].lower() == s[r]:
                    window[ord(s[r]) - ord('a')] -= 1
                else:
                    window[ord(s[r]) - ord('A') + 26] -= 1
                r += 1
            
            else: 
                r += 1

            ct += 1
        return best
        

            



        