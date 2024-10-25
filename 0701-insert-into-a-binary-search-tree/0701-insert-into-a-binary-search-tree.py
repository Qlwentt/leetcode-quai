# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        current = root
        prev = None
        while current:
            if val < current.val:
                prev = current
                current = current.left
                if current == None:
                    prev.left = TreeNode(val)
            else:
                prev = current
                current = current.right
                if current == None:
                    prev.right = TreeNode(val)
                    
        return root
        
                
        
        
    
# Time: O(log(N)) or O(H)
# Space: O(log(N)) or O(H)