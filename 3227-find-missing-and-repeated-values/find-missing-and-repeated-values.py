class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        new=[]
        a=0
        b=0
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                new.append(grid[i][j])
        new.sort()
        fre=Counter(new)
        for i in range(len(new)):
            if fre[new[i]]>=2:
                a=new[i]
                break
        for i in range (1,len(new)+1):
            if (i not in new):
                b=i
                break
        return [a,b]



