from collections import defaultdict, deque
from typing import List

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph  = defaultdict(list)
        indegree = [0]*n
        for par , child in edges:
            graph[par].append(child)
            indegree[child] += 1
        q = deque([i for i in range(n) if indegree[i] == 0])
        ans = [set() for _ in range(n)]
        while q:
            node = q.popleft()
            for child in graph[node]:
                ans[child].add(node)
                ans[child].update(ans[node])  # add parent's ancestors to the child
                indegree[child] -= 1
                if indegree[child] == 0:
                    q.append(child)
        return [sorted(list(s)) for s in ans]
