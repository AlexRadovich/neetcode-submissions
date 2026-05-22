# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):

        self.g = True
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        global good
        good = True

        if not root:
            return True

        def look(self,node):
            l = r = 0
            if node.left:
                l = 1 + look(self,node.left)
            if node.right:
                r = 1 + look(self,node.right)
            height = max(l,r)
            if abs(l-r) > 1: 
                bad()
                good = False
                print("k")
            if not node: height = 0
            return height

        def bad():
            self.g = False
            good = False

            
        look(self,root)
        return self.g

        


        