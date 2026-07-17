class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        found = set()
        solution = []

        def search(ix, cur):



            if ix >= len(nums):
                if str(sorted(cur)) not in found:
                    solution.append(cur[:])
                    found.add(str(sorted(cur)))
                return
        
            search(ix + 1, cur)

            cur.append(nums[ix])
            search(ix + 1, cur)
            cur.pop()

        search(0, [])

        return solution