# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def check(p,q):
            if not p and not q:
                return False
            if p and not q:
                return True
            if q and not p:
                return True
            if p.val != q.val: return True

            if check(p.left,q.left) or check(p.right,q.right):
                return True
            return False
        

        return not check(p,q)