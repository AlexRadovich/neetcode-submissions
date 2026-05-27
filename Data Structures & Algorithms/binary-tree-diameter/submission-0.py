# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.good = True
        self.longest = 0
        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxx = 0


        def search(self,node,maxx):

            if not node: return -1
            

            l = 1 + search(self,node.right,maxx)
            r = 1 + search(self,node.left,maxx)

            height = max(l,r)
            print(node.val,height)
            self.longest = max(self.longest,l+r)

            return height



            
            


        a = search(self,root,maxx)

        return self.longest

            

        