class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        maxval ,  = float("-inf") , 
        output  = [[],[]]
        winners = set([item[0] for item in matches])
        freLosers = Counter([item[1] for item in matches])
        for item in matches:
            maxval = max(maxval,max(item))
        for i in range(1,maxval+1):
            if i in winners or i in freLosers:
                if freLosers[i]==1:
                    output[1].append(i)
                elif( i not in freLosers):
                    output[0].append(i)
        return output

                

