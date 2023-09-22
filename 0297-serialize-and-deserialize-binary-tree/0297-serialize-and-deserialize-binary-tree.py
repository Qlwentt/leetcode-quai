# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        
        preorder = []
        def preorderTraversal(root):
            nonlocal preorder
            if not root:
                preorder.append("N")
                return
            
            preorder.append(str(root.val))
            preorderTraversal(root.left)
            preorderTraversal(root.right)
   
        
        preorderTraversal(root)
        
        return ",".join(preorder)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        preorder = data.split(",")
        preorder.reverse()

        def buildTree():
            if preorder[-1] == "N":
                preorder.pop()
                return None    
            rootVal = int(preorder.pop())
            left = buildTree()
            right = buildTree()
            return TreeNode(rootVal, left, right)
            
        return buildTree()
            
        
        
        
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))