from collections import deque
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
        q = deque([(root,1)])
        res = []
        i = 1
        while q:
            while q and q[0][1] == i:
                node, j = q.popleft()
                if node:
                    res.append(str(node.val))
                    q.append((node.left, j + 1))
                    q.append((node.right, j + 1))
                else:
                    res.append("N")
            i += 1
        print(res)
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        data = data.split(",")
        i = 1
        root = TreeNode(int(data[0]))
        q = deque([root])
        
        while q and i < len(data):
            node = q.popleft()
            if data[i] != 'N':
                left = TreeNode(int(data[i]))
                node.left = left
                q.append(left)
            i += 1
            if data[i] != 'N':
                right = TreeNode(int(data[i]))
                node.right = right
                q.append(right)
            i+= 1
        return root
            
                    

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))