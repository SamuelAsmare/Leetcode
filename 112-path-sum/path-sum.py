# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(curr , target):
            if not curr:
                return False
            if not curr.left and not curr.right:
                if curr.val == target:
                    return True
            target -= curr.val
            return dfs(curr.left , target) or dfs(curr.right , target)
        return dfs(root, targetSum)