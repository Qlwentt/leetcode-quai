# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        sum_ = 0
        
        def preorder(root):
            nonlocal sum_
            if not root:
                return
            
            if root.val in range(low,high+1):
                sum_ += root.val
                
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return sum_