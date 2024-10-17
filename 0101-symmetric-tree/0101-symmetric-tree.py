# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
# Recursive DFS
        if not root.left and not root.right:
            return True
        
        def are_mirrors(root1,root2):
            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False
            
            if root1.val != root2.val:
                return False
            
            left_1_matches_right_2 = are_mirrors(root1.left, root2.right)
            right1_matches_left_2 = are_mirrors(root1.right, root2.left)
            
            return left_1_matches_right_2 and right1_matches_left_2
        
        return are_mirrors(root.left, root.right)
# Time: O(N)
# Space: O(H)

# iterative BFS
        q = collections.deque([root])
        
        while q:
            traversal = []
            for _ in range(len(q)):
                node = q.popleft()
                traversal.append(node.val if node else None)
                if node:
                    q.append(node.left)
                    q.append(node.right)
            if traversal != traversal[::-1]:
                return False
            
        return True

# Time: O(N)
# Space: O(W)
        
        