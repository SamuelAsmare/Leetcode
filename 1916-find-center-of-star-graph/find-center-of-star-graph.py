class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        oneD = [item for rows in edges for item in rows]
        for i in range(len(oneD)):
            if oneD.count(oneD[i] )== len(edges):
                return oneD[i]
             

             
            