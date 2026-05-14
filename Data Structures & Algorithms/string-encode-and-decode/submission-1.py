class Solution:

    def encode(self, strs: List[str]) -> str:
        k = 0
        string = ""
        for i in strs:
            k = len(i)       
            string += (str(k) + "@" + i)
        return string
    def decode(self, s: str) -> List[str]:
        strs = []
        finding = ""
        i=0
        while i < (len(s)):
            if s[i] != "@":
                finding += s[i]
                i += 1
            else:
                print(finding)
                strs.append(s[i + 1:(i+1+int(finding))])                
                i += 1 + int(finding)
                finding = ""

        return strs
