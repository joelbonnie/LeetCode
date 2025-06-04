# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # HashMap
        visitedSet = set()
        while head:
            if head in visitedSet:
                return True
            visitedSet.add(head)
            head = head.next
        
        return False


        # Floyd's Cycle Detection
        s, f = head, head
        while f and f.next:
            s = s.next
            f = f.next.next
            
            if s == f:
                return True
    
        return False
