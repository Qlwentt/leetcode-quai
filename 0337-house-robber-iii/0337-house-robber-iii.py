# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # two choices, rob, not rob
        # DFS returning rob and skip as multiple return
        
        
        def dfs(root):
            if not root: 
                return [0,0] #rob, skip  
                
            left = dfs(root.left)
            right = dfs(root.right)
            
            # rob this node and skip its children
            rob = root.val+left[1]+right[1]
            # skip this node and choose to rob its children or not
            skip = max(left) + max(right)

            
            return [rob,skip]
        return max(dfs(root))
            
            
            
            