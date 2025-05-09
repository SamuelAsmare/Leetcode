class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph =[[] for _ in range(numCourses)]
        que , indegree = deque() , [0 for _ in range(numCourses)]
        ans = []

        for course , pre in prerequisites:
            graph[pre].append(course) # the list of courses which are the pre courses is pointing
            indegree[course]+=1 # indegree(how many courses are pointing this course) 
        
        for pre in range(numCourses): 
            if indegree[pre] == 0:
                que.append(pre)

        while que:
            barren = que.popleft()
            ans.append(barren)
            for child in graph[barren]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    que.append(child)
        if len(ans) != numCourses:
            return False
        return True
            