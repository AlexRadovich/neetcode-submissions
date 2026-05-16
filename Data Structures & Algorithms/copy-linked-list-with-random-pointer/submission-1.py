"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return head
        points = {}

        look = head
        while look:
            points[look] = Node(look.val)
            look = look.next

        j = head
        while j:
            if j.next:
                points[j].next = points[j.next]
            if j.random:
                points[j].random = points[j.random]
            j = j.next
        
        return points[head]
