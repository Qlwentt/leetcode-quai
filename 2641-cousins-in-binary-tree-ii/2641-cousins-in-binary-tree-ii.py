# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = collections.deque([(root, root.val)])
        while q:
            level_nodes = []
            level_sum = 0
            
            for _ in range(len(q)):
                node, node_plus_sib = q.popleft()
                level_nodes.append((node, node_plus_sib ))
                level_sum += node.val
                
                
                if node.left:
                    q.append((node.left, node.left.val + (node.right.val if node.right else 0)))
                    
                if node.right:
                    q.append((node.right, node.right.val + (node.left.val if node.left else 0)))
            
            for current, to_subtract in level_nodes:
                current.val = level_sum - to_subtract
            
        return root
            
            
        