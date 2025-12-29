from typing import List
from collections import defaultdict

class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        rules = defaultdict(list)
        for a, b, c in allowed:
            rules[(a, b)].append(c)
        memo = {}
        def dfs(row: str) -> bool:
            if len(row) == 1:
                return True
            if row in memo:
                return memo[row]
            def build(i , path):
                if i == len(row) - 1:
                    return dfs("".join(path))
                pair = (row[i], row[i + 1])
                if pair not in rules:
                    return False
                for ch in rules[pair]:
                    path.append(ch)
                    if build(i + 1, path):
                        return True
                    path.pop()
                return False
            memo[row] = build(0, [])
            return memo[row]
        return dfs(bottom)
