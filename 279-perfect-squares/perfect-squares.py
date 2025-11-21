class Solution:
    def complete(x):
        return (math.floor(math.sqrt(x)) * math.floor(math.sqrt(x))) == x
    def numSquares(self, n: int) -> int:
        graph = defaultdict(list)
        complete_squares = []
        for i in range(1,n+1):
            x = math.floor(math.sqrt(i))
            if x == i:
                graph[i] = [i]
            else:
                if (complete_squares and  complete_squares[-1] != x*x) or not complete_squares:
                    complete_squares.append(x*x)
                graph[i] = complete_squares.copy()
        q = deque([(n,0)])
        while q:
            num , distance = q.popleft()
            for item in graph[num]:
                if num - item == 0:
                    return distance + 1
                q.append((num-item,distance + 1))
            
                

