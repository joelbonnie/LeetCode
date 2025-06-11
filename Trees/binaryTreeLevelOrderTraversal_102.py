# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        binaryTreeQueue = deque()
        levelOrderTraversal = []
        binaryTreeQueue.append(root)

        while binaryTreeQueue:
            currentLevelNodes = []

            for currentLevelNodeCount in range(0, len(binaryTreeQueue)):
                currentNode = binaryTreeQueue.popleft()
                currentLevelNodes.append(currentNode.val)

                if currentNode.left:
                    binaryTreeQueue.append(currentNode.left)
                if currentNode.right:
                    binaryTreeQueue.append(currentNode.right)

            levelOrderTraversal.append(currentLevelNodes)
        return levelOrderTraversal
                


