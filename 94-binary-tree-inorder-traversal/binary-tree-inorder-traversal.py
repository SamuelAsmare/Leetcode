# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr=[]
        def inorder(o):
            if not o:
                return 
            inorder(o.left)
            arr.append(o.val)
            inorder(o.right)
        inorder(root)
        return arr