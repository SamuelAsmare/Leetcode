class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph=defaultdict(list)
        for i in range(len(roads)):
            loc1 = roads[i][0]
            loc2 = roads[i][1]
            distance = roads[i][2]
            graph[loc1].append([loc2 , distance])
            graph[loc2].append([loc1 , distance])
        visited = set()
        dist = float("inf")
        def dfs(graph , visited , a):
            if a not in visited:
                visited.add(a)
                for items in graph[a]:
                    nonlocal dist
                    dist = min(dist , items[1])
                    dfs(graph , visited , items[0])
        dfs(graph , visited , 1)
        return dist