class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        # we need 3 memory space with 0(n) , graph , dp , 
        graph = defaultdict(list) # build our graph
        in_degree = [0 for _ in range(n)] 
        for pre,post in relations:
            graph[pre].append(post)
            in_degree[post-1] += 1
        dp = [0 for _ in range(n)]
        # lets sort the graph topologically
        q = deque([])
        # mark the time of sources as their time 
        for i in range(n):
            if in_degree[i] == 0:
                q.append(i+1)
                dp[i] = time[i]
        while q:
            node = q.popleft()
            for child in graph[node]:
                in_degree[child-1] -= 1
                dp[child-1] = max(dp[child-1],dp[node-1])
                if in_degree[child-1] == 0:
                    dp[child-1] = dp[child-1] + time[child-1]
                    q.append(child)
        return (max(dp))


