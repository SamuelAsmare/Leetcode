# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        def path(root , string):
            if not root:
                return 
            string = string + str(root.val)+"->" 
            if not root.right and not root.left:
                    ans.append(string)
                    return 
            
            # target -= root.val

            return (path(root.left , string) , path (root.right ,string))
        path(root,"")
        for i in range(len(ans)):
            ans[i] = ans[i][:-2]
        return ans