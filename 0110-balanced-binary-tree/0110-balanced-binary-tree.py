# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def getHeights(root):
            if not root:
                return (0, True)
        
            left, leftBal = getHeights(root.left)
            right, rightBal = getHeights(root.right)
            
            left += 1
            right += 1
            
            height = max(left, right)
            
            isBalanced = leftBal and rightBal and abs(left-right) <= 1
            
            return (height, isBalanced)
        
        return getHeights(root)[1]
            
            