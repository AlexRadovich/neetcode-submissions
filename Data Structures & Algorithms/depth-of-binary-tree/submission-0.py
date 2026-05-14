# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        def recur(root):
            
            l = r = 1
            if(root.left):
                l = 1 + recur(root.left)
               
            if(root.right):
                r = 1 + recur(root.right)
                

            return(max(l,r))

        depth = recur(root)

        return depth