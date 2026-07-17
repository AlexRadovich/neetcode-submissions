class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        solution = []

        end = len(nums) - 1
        
        def search(ix,cur):

            if ix >= end + 1:
                solution.append(cur[:])
                return

            search(ix + 1, cur)
            cur.append(nums[ix])
            search(ix + 1, cur)
            cur.pop()
        search(0,[])

        
        
        return solution