class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        sol = []

        def stack(opens, closes, cur):
            if len(cur) == (n * 2):
                sol.append(cur)
                return


            if opens < n:
                stack(opens + 1, closes, cur + "(")

            if closes < opens:
                stack(opens, closes + 1, cur + ")")

        stack(0,0,"")

        return sol


            