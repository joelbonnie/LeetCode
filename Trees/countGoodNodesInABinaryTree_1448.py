# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        self.goodNodeCount = 0 

        def dfs(currNode, currMax):
            if currNode is None: 
                return  

            if currNode.val >= currMax: 
                self.goodNodeCount += 1
                currMax = currNode.val
                
            dfs(currNode.left, currMax)
            dfs(currNode.right, currMax)

            return  
        
        dfs(root, root.val)
        return self.goodNodeCount

