# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        # stack = []
        # current = root
        # min_diff = float('inf')
        # prev = None
        # while current or stack:
        #     if current:
        #         stack.append(current)
        #         current = current.left
        #     else:
        #         current = stack.pop()
        #         if prev is not None:
        #             min_diff = min(min_diff, abs(prev -current.val))
        #         prev = current.val
        #         current = current.right
        # return min_diff
        
        prev = None
        min_diff = float('inf')
        def inorder(root):
            nonlocal prev, min_diff
            if not root:
                return
            
            inorder(root.left)
            if prev != None:
                min_diff = min(min_diff, abs(prev-root.val))
            prev = root.val
            inorder(root.right)
        
        inorder(root)
        return min_diff
    
        
                
        
        