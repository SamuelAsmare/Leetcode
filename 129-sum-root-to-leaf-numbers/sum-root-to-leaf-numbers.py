# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans , res = [] , 0
        def path(root , string):
            if not root:
                return 
            string = string + str(root.val)
            if not root.right and not root.left:
                    ans.append(string)
                    return 
            
            return (path(root.left , string) , path (root.right ,string))
        
        path(root , "")
        for item in ans:
            res += int(item)
        print(ans , res)
        return res