# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque, defaultdict
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        
        
        # 1. DFS special for left boundary
        # 2. DFS inorder to get leaves from left to right
        # 3. DFS special for right boundary

        
        left = []

        def getLeft(root, parent):
            if not root:
                return
            if not root.left and not root.right:
                return
            left.append(root.val)
            if not root.left:
                if not parent:
                    return
                getLeft(root.right, root)
            else:
                getLeft(root.left, root)
        
        
        leaves = []
        def getLeaves(root):
            if not root:
                return
            getLeaves(root.left)
            if not root.left and not root.right:
                leaves.append(root.val)
            getLeaves(root.right)

        right = []
        def getRight(root, parent):
            if not root:
                return
            if not root.left and not root.right:
                return
            if parent:
                right.append(root.val)
            if not root.right:
                if not parent:
                    return
                getRight(root.left, root)
            else:
                getRight(root.right, root)
        
        getLeft(root, None)
        getLeaves(root)
        getRight(root, None)
        right.reverse()

        return left + leaves + right
        