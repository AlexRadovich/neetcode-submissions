# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        leng = 0
        cur = head
        while(cur):
            leng += 1
            cur = cur.next
        if leng <=2:
            return
        pivot = leng - (leng //2) -1
        
        ix = 0  
        cur = head
        while ix<pivot:
            cur = cur.next
            ix += 1

        second = cur.next
        cur.next = None
       
        
        back = None
        forw = second.next

        while forw:
            second.next = back
            back = second
            second = forw
            forw = forw.next
        second.next = back




        snake = head
        

        while(second):
            hold = second.next
            second.next = snake.next
            snake.next = second
            snake = snake.next.next
            second = hold


                
        while snake:
            print("S",snake.val)
            snake=snake.next
        while second:
            print("B",second.val)
            second = second.next
            
        




        

