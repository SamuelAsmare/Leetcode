# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level_sum = defaultdict(int)
        def dfs(root , level):
            if not root:
                return
            level_sum[level] +=root.val
            dfs(root.left , level + 1)
            dfs(root.right  , level + 1)
        dfs(root , 1)
        ans = 1
        for level in level_sum:
            if level_sum[level] > level_sum[ans]:
                ans = level
        return ans