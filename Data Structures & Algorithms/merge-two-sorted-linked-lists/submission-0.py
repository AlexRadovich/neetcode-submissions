# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        start = ListNode(0)
        cur = start
        l = list1
        r = list2

        while(l or r):
            if not l:
                cur.next = r
                break
            elif not r:
                cur.next = l
                break
            elif(l.val>r.val):
                cur.next = r
                cur = cur.next
                r = r.next
            else:
                cur.next = l
                cur = cur.next
                l = l.next
        return start.next