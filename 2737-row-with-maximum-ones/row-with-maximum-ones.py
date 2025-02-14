class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        index=0
        maxcount=0
        for i in range(len(mat)):
            fre=Counter(mat[i])
            if(fre[1]>maxcount):
                index=i
                maxcount=fre[1]
        return [index, maxcount]