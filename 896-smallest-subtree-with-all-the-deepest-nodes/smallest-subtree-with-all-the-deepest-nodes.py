# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node , level):
            if not node:
                return (node , 0)
            sub_left , left_distance = dfs(node.left , level + 1)
            sub_right , right_distance = dfs(node.right , level + 1)
            if right_distance > left_distance:
                return (sub_right , right_distance + 1)
            if right_distance < left_distance:
                return (sub_left , left_distance + 1)
            else:
                return (node , left_distance + 1)
        ans , _ = dfs(root , 0)
        return ans 
        

