class Solution:
    def __init__(self):
        self.map = {
            2:['a','b','c'],
            3:['d','e','f'],
            4:['g','h','i'],
            5:['j','k','l'],
            6:['m','n','o'],
            7:['p','q','r','s'],
            8:['t','u','v'],
            9:['w','x','y','z'],
        }
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        
        output = []

        def bk(cur, ix):
            print(cur,'HERE: ',ix)
            if ix > len(digits):
                return
            if ix == len(digits):
                output.append(cur)
                return

            for char in self.map[int(digits[ix])]:
                cur += char
                bk(cur,ix+1)
                cur = cur[:-1]


            


        bk('',0)

        return output