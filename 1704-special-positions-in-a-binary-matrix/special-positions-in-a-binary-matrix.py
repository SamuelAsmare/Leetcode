class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        n , m = len(mat) , len(mat[0])
        rows , col = [0]*n , [0]*m
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    rows[i] += 1
                    col[j] += 1
        ans = 0
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1 and rows[i] == 1 and col[j] == 1:
                    ans += 1
        return ans 