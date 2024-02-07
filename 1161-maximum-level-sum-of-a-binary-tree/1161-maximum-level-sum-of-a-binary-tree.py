# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        maxSum = float('-inf')
        q = deque([root])
        smallestMaxLevel = None
        level = 0
        while q:
            levelSum = 0
            level += 1
            for _ in range(len(q)):
                node = q.popleft()
                levelSum += node.val
                
                if node.left:
                    q.append(node.left)
                    
                if node.right:
                    q.append(node.right)
                    
            if levelSum > maxSum:
                smallestMaxLevel = level
                maxSum = levelSum
            
        return smallestMaxLevel