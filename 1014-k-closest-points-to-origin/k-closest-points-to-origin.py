class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        for i in range(len(points)):
            curr=points[i]
            d=points[i][0]*points[i][0] + points[i][1]*points[i][1]
            
            points[i]=[curr,d]
        points=sorted(points,key=lambda x : x[1])
        ans=[]
        for i in range(k):
            ans.append(points[i][0])
        return ans