# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        points = []

        result = ListNode()
        cur = result

        while 1:
            minval = 1001
            minix = -1

            for i in range(len(lists)):
                item = lists[i] 
                if item and item.val <= minval:
                    minval = item.val
                    minix = i

            if minix == -1:
                return result.next

            cur.next = lists[minix]
            lists[minix] = lists[minix].next
            cur = cur.next

            


        