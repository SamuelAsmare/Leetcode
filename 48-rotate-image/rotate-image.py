class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n , maxi , maxj = len(matrix) , 0 , 0
        for i in range(n):
            for j in range(i+1 , n):
                matrix[i][j] , matrix[j][i] = matrix[j][i] , matrix[i][j]
        for item in matrix:
            item.reverse()

        