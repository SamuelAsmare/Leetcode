from collections import defaultdict, deque

class Solution:
    def findAllPeople(self, n, meetings, firstPerson):
        know = {0, firstPerson}
        meetings.sort(key=lambda m: m[2])
        i = 0
        n = len(meetings)
        while i < n:
            time = meetings[i][2]
            group_graph = defaultdict(list)
            people = set()
            while i < n and meetings[i][2] == time:
                x, y, _ = meetings[i]
                group_graph[x].append(y)
                group_graph[y].append(x)
                people.add(x)
                people.add(y)
                i += 1
            queue = deque([p for p in people if p in know])
            visited = set(queue)
            while queue:
                u = queue.popleft()
                for v in group_graph[u]:
                    if v not in visited:
                        visited.add(v)
                        know.add(v)
                        queue.append(v)

        return list(know)
