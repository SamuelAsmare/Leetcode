class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        que , outgraph = deque() , [[] for i in range(len(graph))]
        outdegree , ans = [0 for _ in range(len(graph))] , []
        for i in range(len(graph)):
            for child in graph[i]:
                outgraph[child].append(i)
                outdegree[i] += 1
        for i in range(len(graph)):
            if outdegree[i] == 0:
                que.append(i)
        while que:
            newnode = que.popleft()
            ans.append(newnode)
            for comers in outgraph[newnode]:
                outdegree[comers] -= 1
                if (outdegree[comers] == 0):
                    que.append(comers)
        return sorted(ans)