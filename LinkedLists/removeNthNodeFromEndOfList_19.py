# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # To eventually reach the node BEFORE the node to remove
        dummyNode = ListNode(0, next=head)

        slow, fast = dummyNode, head
        while n:
            fast = fast.next 
            n -= 1
        
        while fast:
            slow = slow.next
            fast = fast.next 
        
        slow.next = slow.next.next 
        return dummyNode.next
