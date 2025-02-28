class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        
        for i in range(left,right+1,+1):
            exists=False
            for j in range(len(ranges)):
                if ((i>=ranges[j][0] and i<=ranges[j][1])):
                    exists=True
                    break
            if(not(exists)):
                return False
            
        return True

            