# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        numGood = 0
        
        def dfs(root, currentMax):
            nonlocal numGood
            if not root:
                return numGood
            
            if root.val >= currentMax:
                numGood += 1
            dfs(root.left, max(root.val, currentMax))
            dfs(root.right, max(root.val, currentMax))
            return numGood
        return dfs(root, float('-inf'))
            