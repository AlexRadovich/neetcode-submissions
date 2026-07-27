# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        cur = [root]

        end = []

        while len(cur) > 0:
            best = -101
            nextt = []

            for thing in cur:
                if thing.left:
                    nextt.append(thing.left)
                if thing.right:
                    nextt.append(thing.right)

                best = max(best, thing.val)

            end.append(best)

            cur = nextt

        return end

        

            

