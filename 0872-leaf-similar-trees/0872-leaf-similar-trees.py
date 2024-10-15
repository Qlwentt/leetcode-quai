# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        
        leaves1 = collections.deque([])
        def inorder_leaves(root):
            if not root:
                return
            inorder_leaves(root.left)
            if not root.left and not root.right:
                leaves1.append(root.val)
            inorder_leaves(root.right)
        
        same = True
        def verify(root):
            nonlocal same
            if not root:
                return 
            
            verify(root.left)
            if not root.left and not root.right:
            
                if not leaves1 or root.val != leaves1.popleft():
                    same = False
            
            verify(root.right)
        inorder_leaves(root1)
        verify(root2)
        return same and len(leaves1) == 0
           