# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = collections.deque([root])
        i = 0
        level = []
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                if i % 2 == 0:
                    level.append(node)
            
            i += 1
            if not level:
                continue
            l = 0
            r = len(level) -1
            
            while l < r:
                l_parent  = level[l]
                r_parent = level[r]
                if not l_parent.left:
                    break
                l_parent.left.val, r_parent.right.val = r_parent.right.val, l_parent.left.val
                
                l_parent.right.val, r_parent.left.val = r_parent.left.val, l_parent.right.val
                l += 1
                r -= 1
            if len(level) == 1:
                node = level[0]
                if node.left:
                    node.left.val, node.right.val = node.right.val, node.left.val
            
        return root
            
        
        