# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        closest = root.val
        
        while root:
            closest = min(root.val, closest, key=lambda x: (abs(x-target), x))
            if root == target:
                return closest
            if root.val > target: # right will have numbers even higher so distance will only get further away, go left
                root = root.left
            else:
                root = root.right
        return closest