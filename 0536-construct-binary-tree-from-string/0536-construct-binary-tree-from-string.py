# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import re
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        if not s:
            return None
        
        s = re.split(r'(\(|\))', s)
        s = [char for char in s if char != ""]
        
        def findParen(start, s):
            open_ = 0
            end = -1
            for i in range(start, len(s)):
                char = s[i]
                if char == "(":
                    open_ += 1
                elif char == ")":
                    open_ -= 1
                if open_ == 0:
                    end = i
                    break
            return start, end
            
        
        def buildTree(s):
            if not s:
                return
            
            root = TreeNode(int(s[0]))
            
            leftStart, leftEnd = findParen(1,s)
            rightStart, rightEnd = findParen(leftEnd+1, s)
            
            root.left = buildTree(s[leftStart+1:leftEnd+1])
            root.right = buildTree(s[rightStart+1:rightEnd+1])
        
            return root
        
        return buildTree(s)
            