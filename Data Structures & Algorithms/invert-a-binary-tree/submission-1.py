# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        k = root
        if not root: return root
        def swap(rt):
            if not rt:
                return
            temp = rt.left
            rt.left = rt.right
            rt.right = temp

            swap(rt.left)
            swap(rt.right)
        swap(root)
        return k