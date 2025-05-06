# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        que , ans = deque([root]) , []
        while que :
            level , n =  [] , len(que) # i am finding the answer for each level 
            for _ in range (n):
                currnode = que.popleft() # current node 
                level.append(currnode.val)
                if currnode.left :
                    que.append(currnode.left)
                if currnode.right :
                    que.append(currnode.right)
            ans.append(level)
        return ans 



