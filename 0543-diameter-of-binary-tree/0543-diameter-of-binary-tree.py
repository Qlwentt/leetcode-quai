# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        maxDiameter = 0
        
        def diameter(root):
            if not root:
                return 0
            
            nonlocal maxDiameter

            left = diameter(root.left)
            right = diameter(root.right)

            leftPath = left + 1 if root.left else left
            rightPath = right + 1 if root.right else right
            
            maxDiameter = max(maxDiameter, leftPath + rightPath)
            
            return max(leftPath, rightPath)
        diameter(root) 
        return maxDiameter
        
        
        