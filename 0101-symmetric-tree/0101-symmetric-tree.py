# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right:
            return True
        
        def are_mirrors(root1,root2):
            val1 = root1.val if root1 else float('-inf')
            val2 = root2.val if root2 else float('-inf')
    
            if val1 != val2:
                return False
            if val1 == float('-inf'):
                return True
            
            left = are_mirrors(root1.left, root2.right)
            right = are_mirrors(root1.right, root2.left)
            
            return left and right
        
        return are_mirrors(root.left, root.right)

# iterative BFS
#         q = collections.deque([root])
        
#         while q:
#             traversal = []
#             for _ in range(len(q)):
#                 node = q.popleft()
#                 traversal.append(node.val if node else None)
#                 if node:
#                     q.append(node.left)
#                     q.append(node.right)
#             if traversal != traversal[::-1]:
#                 return False
            
#         return True
        
        
        