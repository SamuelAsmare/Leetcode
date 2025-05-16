# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        def levelorder(root):
            que , result  = deque([root]) , []
            while que:
                temp  = [] 
                for i in range(len(que)):
                    curr = que.popleft()
                    temp.append(curr.val)
                    if curr.left:
                        que.append(curr.left)
                    if curr.right:
                        que.append(curr.right)
                result . append (temp)
            result.reverse()
            return result
        return levelorder(root)

                    