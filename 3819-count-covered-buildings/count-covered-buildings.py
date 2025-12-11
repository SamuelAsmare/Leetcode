class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        horizontals = defaultdict(list)
        verticals = defaultdict(list)
        for x , y in buildings:
            horizontals[y].append(x)
            verticals[x].append(y)
        ans = 0
        for item in horizontals:
            horizontals[item].sort()
        for item in verticals:
            verticals[item].sort()
        for x , y in buildings:
            if len(horizontals[y]) <= 2:
                continue
            if len(verticals[x]) <= 2:
                continue
            if x == horizontals[y][-1] or x == horizontals[y][0]:
                continue
            if y == verticals[x][-1] or y == verticals[x][0]:
                continue
            ans +=1
        return ans



