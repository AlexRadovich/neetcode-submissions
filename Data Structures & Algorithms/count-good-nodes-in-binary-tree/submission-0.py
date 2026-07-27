# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        num = 0
        

        def rec(node, best):
            if not node: return 0

            self = 0
            if node.val >= best:
                self = 1
                print(node.val)

            best = max(best, node.val)

            
            return self + rec(node.left, best) + rec(node.right, best)

        num = rec(root, -101)

        return num