# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Do an in-order traversal 

        nodeStack = []
        current = root

        while nodeStack or current:
            
            while current:
                nodeStack.append(current)
                current = current.left 
            
            # current is null - backstrack 
            
            current = nodeStack.pop()
            if k == 1:
                return current.val 
            else: 
                k -= 1
            
            current = current.right 

                
            
