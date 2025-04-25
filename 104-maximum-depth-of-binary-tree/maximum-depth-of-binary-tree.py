# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def find_max(node):
            if not node : 
                return 0 
            return 1 + max(find_max(node.right),find_max(node.left)) 
        return find_max(root)    