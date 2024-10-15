# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
#         if not root1 and not root2:
#             return None
#         if not root1 and root2:
#             return root2
#         if not root2 and root1:
#             return root1
        
#         answer = TreeNode()
#         q = collections.deque([(root1, root2, answer)])
        
#         while q:
#             node1, node2, current = q.popleft()
#             val1 = node1.val if node1 else 0
#             val2 = node2.val if node2 else 0
#             current.val = val1+val2
            
#             left1 = node1.left if node1 else None
#             left2 = node2.left if node2 else None
            
#             right1 = node1.right if node1 else None
#             right2 = node2.right if node2 else None
            
#             if not left1 and not left2:
#                 current.left = None
#             else:
#                 current.left = TreeNode()
#                 q.append((left1, left2, current.left))
                
#             if not right1 and not right2:
#                 current.right = None
#             else:
#                 current.right = TreeNode()
#                 q.append((right1, right2, current.right))
        
#         return answer
        def dfs(root1, root2):
            if not root1 and not root2:
                return None
            
            val1 = root1.val if root1 else 0
            val2 = root2.val if root2 else 0
            
            left1 = root1.left if root1 else None
            left2 = root2.left if root2 else None
            
            right1 = root1.right if root1 else None
            right2 = root2.right if root2 else None 
            
            new_root = TreeNode(val1+val2)
            new_root.left = dfs(left1, left2)
            new_root.right = dfs(right1, right2)

            return new_root
        
        return dfs(root1,root2)
                
            
            
        
        