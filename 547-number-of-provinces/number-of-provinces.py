class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph , n , visited , provinces = defaultdict(set) , len(isConnected) , set() , 0
        for i in range(n):
            for j in range(n):
                curr  =  isConnected[i][j]
                if curr==1:
                    graph[i+1].add(j+1)
                    graph[j+1].add(i+1)
        def dfs(graph,char,visited):
            if char in visited:
                return         
            visited.add(char)
            for j in graph[char]:
                dfs(graph,j,visited)
        for each in graph:
            if each not in visited:
                dfs(graph,each,visited)
                provinces += 1
        return provinces
        

