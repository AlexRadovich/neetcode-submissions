class Solution:
    def countBits(self, n: int) -> List[int]:
        k = []
        for i in range(n+1):
            ones = 0
            s = i
            while s >= 1:
                if s % 2 == 1:
                    ones += 1
                s = s // 2
            k.append(ones)
        return k