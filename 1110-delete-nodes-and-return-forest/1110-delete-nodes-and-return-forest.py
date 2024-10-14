# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        answer = set([])
        def delete(root):
            if not root:
                return
            
            left = delete(root.left)
            right = delete(root.right)
            
            root.left = left
            root.right = right
            
            if root.val in to_delete:
                answer.discard(root)
                if root.left:
                    answer.add(root.left)
                if root.right:
                    answer.add(root.right)
                return None
            else:
                return root
        new_root = delete(root)
        if new_root:
            answer.add(new_root)
        return answer
        
        
            
                    
            
                
    
        
        
        
        