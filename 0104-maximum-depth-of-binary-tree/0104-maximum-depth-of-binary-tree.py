# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
# recursive DFS solution
        if not root:
            return 0
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        
        return max(left, right) + 1
# Time: O(N)
# Space: O(H) H is height of the tree

# BFS solution
        if not root:
            return 0
        q = collections.deque([root])
        level = 0
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                
                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
            level += 1
        return level
    
# Time: O(N)
# Space: O(W) W is width of largest level
            


            
        