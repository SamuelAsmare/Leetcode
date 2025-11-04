class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        if "0000" in dead:
            return -1
        def neighbors(code):
            res = []
            for i in range(4):
                x = int(code[i])
                for d in (-1, 1):
                    y = (x + d) % 10
                    res.append(code[:i] + str(y) + code[i+1:])
            return res
        queue = deque([("0000", 0)])  
        visited = {"0000"}
        while queue:
            code, steps = queue.popleft()
            if code == target:
                return steps
            for nxt in neighbors(code):
                if nxt not in visited and nxt not in dead:
                    visited.add(nxt)
                    queue.append((nxt, steps + 1))
        return -1
