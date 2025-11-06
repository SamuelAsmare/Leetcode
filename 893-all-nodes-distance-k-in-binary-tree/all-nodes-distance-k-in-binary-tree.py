# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if k == 0:
            return [target.val]
        # bfs for constructing our graph
        q = deque([root])
        parent = defaultdict(list)
        while q:
            node = q.popleft()
            if node.left:
                parent[node.left.val].append(node.val)
                parent[node.val].append(node.left.val)
                q.append(node.left)
            if node.right:
                parent[node.right.val].append(node.val)
                parent[node.val].append(node.right.val)
                q.append(node.right)
        # bfs for finding the k distance nodes
        q = deque([(target.val,0)])
        ans = []
        seen = set([target.val])
        while q:
            node , distance = q.popleft()
            if distance == k:
                ans.append(node)
            for item in parent[node]:
                if item not in seen:
                    seen.add(item)
                    q.append((item , distance+1))
        return ans 
                



        