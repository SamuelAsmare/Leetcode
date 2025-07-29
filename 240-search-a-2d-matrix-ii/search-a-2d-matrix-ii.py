class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        exist=False
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if(matrix[i][j] ==target):
                    exist=True
                    break
                elif(matrix[i][j]>target):
                    break
            if(exist):
                break
        return exist