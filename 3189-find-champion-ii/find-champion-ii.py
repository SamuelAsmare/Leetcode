class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        # i will use graph dfs then i will check if that element is existed in the visited, then if 
        if n==1 and len(edges)==0:
            return  0
        def dfs(graph,a,visited):
            if a not in visited:
                visited.add(a)
                for  neighbour in graph[a]:
                    dfs(graph,neighbour,visited)
        strong,weak,graph=set(),set(),defaultdict(list)
        for i,j in edges:
            strong.add(i)
            weak.add(j)
            graph[i].append(j)
        visited,candidate=set(),[]
        for i in strong:
            if (i not in weak):
                candidate.append(i)
                break
        print(candidate)
        for item in candidate:
            dfs(graph,item,visited)
        print(visited)
        if len(visited)==n:
                return candidate[0]
        return -1
                  
        

