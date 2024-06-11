# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        num_set = set()
        def build_dict(root):
            if not root:
                return
            num_set.add(root.val)
            build_dict(root.left)
            build_dict(root.right)
        build_dict(root1)
        def find(root):
            if not root:
                return False
            
            left = find(root.left)
            right = find(root.right)
            
            return left or right or target - root.val in num_set
        return find(root2)
            