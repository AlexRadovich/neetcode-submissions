# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def __init__(self):
        self.ct = 0
        self.ret = 0

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def dfs(node):

            if not node:
                return

            dfs(node.left)
            self.ct += 1
            if self.ct == k:
                self.ret = node.val
            dfs(node.right)

            return

        dfs(root)

        return self.ret