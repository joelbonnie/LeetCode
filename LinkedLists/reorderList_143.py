# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # Find the middle of the linked list
        s,f = head, head.next 
        while f and f.next:
            f = f.next.next 
            s = s.next 
        
        second = s.next
        s.next = None

        # Reverse second part of the linked list 
        prev = None
        while second: 
            temp = second.next 
            second.next = prev
            prev = second 
            second = temp 
        
        # Join together 
        
        next_l = None
        next_r = None

        while prev: 
            next_l = head.next
            next_r = prev.next

            head.next = prev
            prev.next = next_l

            head = next_l
            prev = next_r 




