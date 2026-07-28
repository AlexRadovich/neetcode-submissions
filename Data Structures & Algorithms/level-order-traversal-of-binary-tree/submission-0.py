# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def __init__(self):
        self.q = []
        self.end = []

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root: return []

        ret = []
        step = [root]

        while 1:
            vals = []
            step_copy = []
            for thing in step:
                if thing:
                    vals.append(thing.val)

            if len(vals) > 0:
                ret.append(vals)

            for item in step:
                if item:
                    step_copy.append(item.left)
                    step_copy.append(item.right)

                
            if len(step_copy)==0:
                break

            step = step_copy

        return ret