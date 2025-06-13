# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sumNode = ListNode()
        carry = 0

        sumNodeBuild = sumNode 
        while l1 is not None or l2 is not None:
            firstNum = l1.val if l1 else 0 
            secondNum = l2.val if l2 else 0 

            digitSum = firstNum + secondNum + carry 
            sumNodeBuild.next = ListNode(digitSum % 10)
            carry = digitSum // 10 

            if l1: l1 = l1.next 
            if l2: l2 = l2.next
            sumNodeBuild = sumNodeBuild.next

        if carry: 
            sumNodeBuild.next = ListNode(carry)
        
        return sumNode.next
