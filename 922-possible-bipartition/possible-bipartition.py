class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = {i: [] for i in range(1, n + 1)}
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
        groups = {}  
        def dfs(node, c):
            if node in groups:
                return groups[node] == c
            groups[node] = c
            for nei in graph[node]:
                if not dfs(nei, 1 - c):
                    return False
            return True
        for i in range(1, n + 1):
            if i not in groups:
                if not dfs(i, 0):
                    return False
        return True
