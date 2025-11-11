class Solution:
    def checkIfPrerequisite(self, numCourses: int, pre: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # topological sort (kahn's algorithm)
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for a , b in pre:
            graph[a].append(b)
            indegree[b] += 1
        q = deque([i for i in range(numCourses) if indegree[i]==0])
        ans = [set() for _ in range(numCourses)]
        print(q)
        while q :
            node = q.popleft()
            for b in graph[node]:
                ans[b].update(ans[node])
                ans[b].add(node)
                indegree[b]-=1
                if indegree[b] == 0:
                    q.append(b)
        result = []
        for u , v in queries:
            result.append(u in ans[v])
        return result





