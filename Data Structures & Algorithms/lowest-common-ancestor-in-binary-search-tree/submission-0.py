# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        val1 , val2 = p.val, q.val

        cur = root
        while cur.val > max(val1,val2) or cur.val < min(val1,val2):
            if cur.val > max(val1,val2):
                cur = cur.left
            elif cur.val < min(val1,val2):
                cur = cur.right

        return cur