class Solution:
    def findRestaurant(self , a, b):
        d = {v: i for i, v in enumerate(a)}
        res, minsum = [], float('inf')
        for j, v in enumerate(b):
            if v in d:
                s = j + d[v]
                if s < minsum:
                    res, minsum = [v], s
                elif s == minsum:
                    res.append(v)
        return res
