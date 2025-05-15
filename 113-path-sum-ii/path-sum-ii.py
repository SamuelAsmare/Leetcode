# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        def path(root , target , arr):
            if not root:
                return 
            arr = arr + [root.val]
            if not root.left and not root.right :
                if target == root.val:
                    ans.append(arr)
                return 
            target -= root.val
            return (path(root.left , target , arr) , path(root.right , target , arr))
        path(root , targetSum , [])
        return ans
