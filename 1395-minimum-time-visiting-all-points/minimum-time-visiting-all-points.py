class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans  , n = 0 , len(points)
        if n == 1:
            return 0
        for i in range(n-1):
            x1 , y1 = points[i]
            x2 , y2 = points[i+1]
            ans += max(abs(x1 - x2) , abs(y1 - y2))
        return ans


            