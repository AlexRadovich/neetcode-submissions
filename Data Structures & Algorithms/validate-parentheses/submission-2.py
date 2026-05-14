class Solution:
    def isValid(self, s: str) -> bool:
        k = []
        l ={
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }
        for i in range(len(s)):

            if s[i]=='(' or s[i] == '{' or s[i] == '[':
                k.append(s[i])
            elif len(k) > 0:
                top = k.pop()
                if top != l.get(s[i]):
                    return False
            else:
                return False
            
        return len(k) == 0

