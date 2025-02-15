class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        found=False
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if(matrix[i][j] ==target):
                    found=True
                    break
                elif(matrix[i][j]>target):
                    break
            if(found):
                break
        return found