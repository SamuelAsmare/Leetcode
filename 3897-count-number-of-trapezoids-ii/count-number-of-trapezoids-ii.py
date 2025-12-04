class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        n = len(points)
        slope_intercept = defaultdict(list)
        mid_slope = defaultdict(list)
        ans = 0
        #  first we have to get the slope and all itercepts
        for i in range(n):
            x1 , y1 = points[i]
            for j in range(i + 1,n):
                x2 , y2 = points[j]
                dx , dy  , b , slope  = x2 - x1 , y2 - y1, x1 , float("inf")
                if x1 != x2 :
                    slope = (dy/dx)
                    b =  (y1 * dx - x1 * dy) / dx
                slope_intercept[slope].append(b)
                mid_slope[((x1 + x2)/2 , (y1 + y2)/2)].append(slope)
        for intercepts in slope_intercept.values():
            if len(intercepts) == 1:
                continue
            cnt = Counter(intercepts)
            prefix = 0
            for val in cnt.values():
                ans += (prefix * val)
                prefix += val
        # count parallelograms and subtract from the answer
        # two lines with same midpoint and different slope make parallelogram
        for s in mid_slope.values():
            if len(s) == 1 : continue
            cnt = Counter(s)
            prefix = 0
            for item in cnt.values():
                ans -= (item * prefix)
                prefix += item
        return ans

            


        