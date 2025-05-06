# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        que ,  ans , stair = deque ([root]) , [] , 1
        while que :
            level , n = [] , len (que)
            for _ in range(n):
                node = que.popleft()
                level.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)      
            if stair % 2 == 0:
                    level.reverse()  
            stair += 1    
            ans.append(level)
            print (stair)
        return ans