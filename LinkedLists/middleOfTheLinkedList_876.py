# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        listLen = 0 
        tempHead = head
        while tempHead:
            listLen += 1
            tempHead = tempHead.next 
        
        steps = ((listLen - 1) / 2) if listLen % 2 == 1 else (listLen / 2)
        while steps:
            steps -=1 
            head = head.next 
        return head
