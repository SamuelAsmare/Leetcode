class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        first, second  , ans  =  0 , 0 , []
        while first < len(firstList) and second < len(secondList):
            start1, end1 = firstList[first] # unpack
            start2, end2 =  secondList[second] # unpack
            start , end  = max(start1, start2) ,  min(end1, end2)
           
            if start <= end: # if the start is grather than or equal to the end ,
                ans.append([start, end])
            if end1 < end2: # if the first end is larger than the second end i am increasing..
                first += 1 
            else: 
                second += 1
        return ans