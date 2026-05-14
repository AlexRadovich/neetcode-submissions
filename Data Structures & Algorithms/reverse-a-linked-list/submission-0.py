# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        dummy = None
        cur = head
        nxt = head.next
        while cur.next:
            print(0)
            cur.next = dummy
            dummy = cur
            cur = nxt
            nxt = nxt.next
        cur.next = dummy
        return cur
