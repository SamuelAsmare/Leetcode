class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        Sum,n=0,len(mat)
        if(n%2!=0):
            Sum-=mat[(n-1)//2][(n-1)//2]
        for i in range(len(mat)):
            Sum+=mat[i][i]
            Sum+=mat[i][n-i-1]
        return Sum
