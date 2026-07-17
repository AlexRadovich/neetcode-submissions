class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        solution = []

        found = set()

        candidates.sort()

        def dfs(ix, cur, summ):

            if summ > target: return

            if summ == target:
                solution.append(cur[:])
                return
            
            if ix == len(candidates):
                return

            

            cur.append(candidates[ix])
            
            dfs(ix + 1, cur, summ + candidates[ix])
            cur.pop()

            while ix < len(candidates) - 1 and candidates[ix] == candidates[ix +1]:
                ix += 1
            dfs(ix + 1, cur, summ)
        
        dfs(0,[], 0)

        return solution
            