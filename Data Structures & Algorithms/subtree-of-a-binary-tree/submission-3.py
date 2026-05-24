# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   

    def __init__(self):
        self.issub = False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def look(self, node1, node2):
            if not node1:return
            if compare(self,node1,node2): 
                self.issub = True
            else:
                look(self,node1.left,node2)
                look(self,node1.right,node2)
            



        def compare(self, t1, t2):

            if not t1 and not t1: return True
            if t1 and not t2: return False
            if not t1 and t2: return False
            if t1.left and not t2.left: return False
            if not t1.left and  t2.left: return False
            if t1.right and not t2.right: return False
            if not t1.right and  t2.right: return False


            if t1.val != t2.val: return False
            return compare(self, t1.left , t2.left) and compare(self,t1.right , t2.right)



        look(self, root, subRoot)

        return self.issub



