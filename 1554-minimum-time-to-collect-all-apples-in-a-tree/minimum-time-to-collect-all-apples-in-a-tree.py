from collections import defaultdict

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        def dfs(node, parent):
            time = 0
            for nei in graph[node]:
                if nei != parent:
                    time += dfs(nei, node)
            if (time > 0 or hasApple[node]) and node != 0:
                return time + 2 
            return time
        return dfs(0, -1)
