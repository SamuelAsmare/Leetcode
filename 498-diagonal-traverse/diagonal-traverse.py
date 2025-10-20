class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        up_down = 1 
        rows, cols = len(mat), len(mat[0])
        res = []
        i, j = 0, 0
        for _ in range(rows*cols):
            res.append(mat[i][j])
            if up_down == 1:
                if(j == cols - 1):
                    i+=1
                    up_down = -1
                elif(i == 0):
                    j+=1
                    up_down = -1
                else:
                    i-=1
                    j+=1
            else:
                if(i == rows -1):     
                    j+=1
                    up_down = 1
                elif(j == 0):        
                    i+=1
                    up_down = 1
                else:
                    i+=1
                    j-=1
        return res
