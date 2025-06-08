# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxPathLength = 0 

        def dfs(root: Optional[TreeNode]) -> int: 
            if not root: 
                return 0 
            leftHeight = dfs(root.left)
            rightHeight = dfs(root.right)
            self.maxPathLength = max(self.maxPathLength, leftHeight + rightHeight)
            return 1 + max(leftHeight, rightHeight)
        
        dfs(root)
        return self.maxPathLength 

