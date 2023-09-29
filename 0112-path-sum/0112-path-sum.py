# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def pathSum(root, curSum):
            if not root:
                return False

            curSum += root.val
            if not root.left and not root.right:
                return curSum == targetSum

            if pathSum(root.left, curSum):
                return True
            return pathSum(root.right, curSum)
        return pathSum(root, 0)