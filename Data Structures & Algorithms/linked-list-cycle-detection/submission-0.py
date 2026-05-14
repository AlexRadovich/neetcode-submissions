# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        k = set()
        cur = head
        while(cur.next):
            if cur in k:
                return True
            k.add(cur)
            cur = cur.next
        return False