# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
#         def get_height(root, to_remove):
#             if not root:
#                 return -1
            
#             left = get_height(root.left, to_remove)
#             right = get_height(root.right, to_remove)
            
#             if root.val == to_remove:
#                 return -1
            
#             return max(left, right) + 1
        
#         answer = []
#         for query in queries:
#             height = get_height(root, query)
#             answer.append(height)
#         return answer
        max_height_after_removal = [0] * 100001
        self.current_max_height = 0

        def _traverse_left_to_right(node, current_height):
            if not node:
                return

            # Store the maximum height if this node were removed
            max_height_after_removal[node.val] = self.current_max_height

            # Update the current maximum height
            self.current_max_height = max(
                self.current_max_height, current_height
            )

            # Traverse left subtree first, then right
            _traverse_left_to_right(node.left, current_height + 1)
            _traverse_left_to_right(node.right, current_height + 1)

        def _traverse_right_to_left(node, current_height):
            if not node:
                return

            # Update the maximum height if this node were removed
            max_height_after_removal[node.val] = max(
                max_height_after_removal[node.val], self.current_max_height
            )

            # Update the current maximum height
            self.current_max_height = max(
                current_height, self.current_max_height
            )

            # Traverse right subtree first, then left
            _traverse_right_to_left(node.right, current_height + 1)
            _traverse_right_to_left(node.left, current_height + 1)

        _traverse_left_to_right(root, 0)
        self.current_max_height = 0  # Reset for the second traversal
        _traverse_right_to_left(root, 0)
        
        return [max_height_after_removal[q] for q in queries]