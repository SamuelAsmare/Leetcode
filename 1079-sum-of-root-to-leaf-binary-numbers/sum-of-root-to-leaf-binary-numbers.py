# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        paths , ans = [] , 0
        def dfs(node , path):
            path = path + str(node.val)
            if node.left:
                dfs(node.left , path)
            if node.right:
                dfs(node.right , path)
            if not node.left and not node.right:
                paths.append(path)
        dfs(root , "")
        for item in paths:
            ans += int(item,2)
        return ans

