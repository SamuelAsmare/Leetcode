from collections import defaultdict
from typing import List

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = defaultdict(list)
        for rich, poor in richer:
            graph[poor].append(rich)
        ans = [-1] * n  
        def dfs(x):
            if ans[x] != -1:  
                return ans[x]
            ans[x] = x  
            for rich in graph[x]:
                candidate = dfs(rich)
                if quiet[candidate] < quiet[ans[x]]:
                    ans[x] = candidate
            return ans[x]
        for i in range(n):
            dfs(i)
        return ans
