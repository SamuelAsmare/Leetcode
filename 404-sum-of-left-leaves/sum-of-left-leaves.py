# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        arr=[]
        def check(o):
            if (not o):
                return 
            check(o.left)
            if o.left:
                if (not o.left.left and not o.left.right):
                    arr.append(o.left.val)
            check(o.right)
        check(root)
        return sum(arr)
            
        