class Solution:
    def buildMatrix(self, k: int, rowConditions: list[list[int]], colConditions: list[list[int]]) -> list[list[int]]:
        def topoSort(graph):
            in_degree = [0] * k
            for node in range(k):
                for neighbor in graph[node]:
                    in_degree[neighbor] += 1
            queue = deque(i for i, d in enumerate(in_degree) if d == 0)
            result = []
            while queue:
                node = queue.popleft()
                result.append(node)
                for neighbor in graph[node]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        queue.append(neighbor)
            return result if len(result) == k else []
        row_graph = [[] for _ in range(k)]
        col_graph = [[] for _ in range(k)]
        for start, end in rowConditions:
            row_graph[start-1].append(end-1) 
        for start, end in colConditions:
            col_graph[start-1].append(end-1) 
        row_order = topoSort(row_graph)
        col_order = topoSort(col_graph)
        if not row_order or not col_order:
            return []
        matrix = [[0] * k for _ in range(k)]
        for value in range(k):
            r, c = row_order.index(value), col_order.index(value)
            matrix[r][c] = value + 1 

        return matrix
