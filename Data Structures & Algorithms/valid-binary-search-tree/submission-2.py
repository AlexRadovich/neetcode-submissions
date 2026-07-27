# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.flag = True
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def recur(node,minn,maxx):
            if not node: return

            if node.val <= minn or node.val >= maxx:
                self.flag = False
                return

            recur(node.left, minn, node.val)
            recur(node.right, node.val, maxx)

            return

            

            
        recur(root, float("-inf") , float("inf"))
        return self.flag

            