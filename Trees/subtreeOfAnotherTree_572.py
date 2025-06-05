# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isSameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool: 
        if not root and not subRoot: 
            return True 
        elif root and subRoot and root.val == subRoot.val: 
            return self.isSameTree(root.left, subRoot.left) and self.isSameTree(root.right, subRoot.right)
        return False 

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True 
        elif not root: 
            return False
        elif self.isSameTree(root, subRoot):
            return True 
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
