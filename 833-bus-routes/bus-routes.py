class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        graph = defaultdict(set)
        for bus , route in enumerate(routes):
            for stop in route:
                graph[stop].add(bus)
        # our graph is ready
        # now start our BFS
        q = deque([(source,0)])
        visited_bus = set()
        visited_stop = set()
        while q:
            stop , number_bus = q.popleft()
            if stop == target:
                return number_bus
            for bus in graph[stop]:
                if bus not in visited_bus:
                    visited_bus.add(bus)
                    for item in routes[bus]:
                        if item not in visited_stop:
                            visited_stop.add(item)
                            q.append((item,number_bus+1))
        return -1
