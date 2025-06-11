# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []

        rightSideView = []
        treeQueue = deque()
        treeQueue.append(root)
        
        while treeQueue:
            currentLevel = []
            for i in range(len(treeQueue)):
                currentNode = treeQueue.popleft()
                currentLevel.append(currentNode)
                if currentNode.left: treeQueue.append(currentNode.left)
                if currentNode.right: treeQueue.append(currentNode.right)
            
            rightSideView.append(currentLevel[-1].val)
        
        return rightSideView

