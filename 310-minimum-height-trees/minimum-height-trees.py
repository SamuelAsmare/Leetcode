class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # BFS starting from the leaves
        if n <= 2:
            return [i for i in range(n)]
        graph = defaultdict(list)
        neighbours = [0 for _ in range(n)]
        for a , b in edges:
            graph[a].append(b)
            graph[b].append(a)
            neighbours[a] += 1
            neighbours[b] += 1
        q = deque([i for i in range(n) if neighbours[i] == 1])
        # traverse until i get max of 2 nodes ,  since a graph can have maximum of 2 centers
        while q :
            if n <= 2:
                return  list(q)
            for _ in range(len(q)):
                node = q.popleft()
                n -= 1
                for nei in graph[node]:
                    neighbours[nei] -= 1
                    if neighbours[nei] == 1:
                        q.append(nei)
        



