class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        fin = []
        dicct = {}
        ct = 0
        for i in (strs):
            k = [0] * 26
            for letter in i:
                k[ord(letter)-ord('a')] += 1
            k = str(k)
            
            if k in dicct:
                fin[dicct.get(k)].append(i)
            else:            
                dicct[k] = ct
                ct += 1
                fin.append([i])

        return fin