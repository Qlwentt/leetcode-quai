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
        q = deque([(root, 1)])
        ansLevel = None
        while q:
            curSum = 0
            for _ in range(len(q)):
                node, level = q.popleft()
                curSum += node.val
                
                if node.left:
                    q.append((node.left, level + 1))
                
                if node.right:
                    q.append((node.right, level + 1))
            if curSum > maxSum:
                maxSum = curSum
                ansLevel = level
        
        return ansLevel
        
        