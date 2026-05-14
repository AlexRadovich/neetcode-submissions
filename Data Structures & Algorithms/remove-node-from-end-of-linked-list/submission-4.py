# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or n<=0: return head
        if not head.next: return None
        l = head
        r = head


        for _ in range(n):
            if(r.next):
                r = r.next
            else:
                return head.next
        while r.next:
            l = l.next
            r = r.next
        print(l.val,r.val)

        l.next = l.next.next
        
        

        return head