# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        answer = 0
        def dfs(root):
            nonlocal answer
            if not root:
                return [0, 0]
            
            
            numL, sumL = dfs(root.left)
            numR, sumR = dfs(root.right)
            
            totalNum = numL + numR + 1
            totalSum = sumL + sumR + root.val
            
            answer = max(answer, totalSum/totalNum)
            
            return [totalNum, totalSum]
        
        dfs(root)
        return answer
            
            
        