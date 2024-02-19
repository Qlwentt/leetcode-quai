# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1
        q = deque([root])
        maxSum = float('-inf')
        level = 0
        answer = 0
        while q:
            runSum = 0
            level += 1
            for _ in range(len(q)):
                node = q.popleft()
                runSum += node.val
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if runSum > maxSum:
                maxSum = runSum
                answer = level
        return answer
            