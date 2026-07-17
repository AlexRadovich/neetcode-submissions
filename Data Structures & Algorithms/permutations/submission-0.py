class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        solution = []

        end = len(nums)

        def search(ix, cur, found):
            print(cur, ix, [i for i in found])

            if len(cur) == end:
                solution.append(cur[:])
                return

            found.add(ix)

            for i in range(len(nums)):
                if i not in found:
                    cur.append(nums[i])
                    search(i, cur, found)
                    cur.pop()
            found.remove(ix)
            
        for i in range(len(nums)): 

            search(i, [nums[i]], set())

        return solution

