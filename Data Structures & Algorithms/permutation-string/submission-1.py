class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        find = set(s1)
        n = len(s1)

        letters = [0] * 26
        for i in s1:
            letters[ord(i)-ord('a')] += 1
        sh = hash(tuple(letters))

        letters2 = [0] * 26

        l,r = 0,n-2


        for i in range(n-1):
            letters2[ord(s2[i])-ord('a')] += 1
        print(letters)
        print(letters2)
        while r < len(s2)-1:

            r += 1
            letters2[ord(s2[r])-ord('a')] += 1
            if sh == hash(tuple(letters2)):
                return True
            letters2[ord(s2[l])-ord('a')] -= 1
            print(f"step: {letters2}")
            l += 1
        return False



