# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        maxSum = float('-inf')
        ansLevel = None
        curLevel = 0
        while q:
            curSum = 0
            curLevel += 1
            for _ in range(len(q)):
                node = q.popleft()
                curSum += node.val
                
                if node.left:
                    q.append(node.left)
                    
                if node.right:
                    q.append(node.right)
            if curSum > maxSum:
                ansLevel = curLevel
            maxSum = max(maxSum, curSum)
        
        return ansLevel
        