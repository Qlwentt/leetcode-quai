# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        parents = {root:None}
        def dfs(root):
            if not root:
                return 
            if root.left:
                parents[root.left] = root
                dfs(root.left)
            if root.right:
                parents[root.right] = root
                dfs(root.right)
        
        def isGoodNode(node,parents):
            val = node.val
            while node:
                parentVal = parents[node].val if parents[node] else float('-inf')
                if parentVal > val:
                    return False
                node = parents[node]
            return True
        
        dfs(root)
        result = 0
        for node in parents:
            if isGoodNode(node, parents):
                result += 1
        return result
        
            