# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        numbers = []
        number = []
        def visitLeaves(root):
            if root:
                number.append(str(root.val))
                if not root.left and not root.right:
                    numbers.append("".join(number))
                visitLeaves(root.left)
                visitLeaves(root.right)
                number.pop()
        visitLeaves(root)
        return sum([int(num) for num in numbers])