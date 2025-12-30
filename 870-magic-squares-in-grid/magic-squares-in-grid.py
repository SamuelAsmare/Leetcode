class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        row , col , ans  = len(grid) , len(grid[0]) , 0
        if row < 3 or col < 3 :
            return 0
        # total = row - 2 * col - 2     1 2 3 4 5 
        #  try each submatrix               2 
        for i in range(2 , row):
            start_row = i - 2
            for j in range(2 , col):
                start_col = j - 2
                #  the resulting matrix
                fre = Counter(grid[row][col] for row in range(start_row, i+1) for col in range(start_col, j+1))
                if len(fre) < 9:
                    continue
                for k in range(1,10):
                    if fre[k] == 0:
                        break                       
                else:
                    matrix = [row[start_col : start_col + 3] for row in grid[start_row : start_row + 3]]
                    if matrix[0][1] + matrix[0][2] != matrix[1][0] + matrix[2][0]:
                        continue
                    if matrix[0][0] + matrix[0][2] != matrix[1][1] + matrix[2][1]:
                        continue
                    if matrix[0][0] + matrix[0][1] != matrix[1][2] + matrix[2][2]:
                        continue
                    if matrix[0][0] + matrix[2][2] != matrix[2][0] + matrix[0][2]:
                        continue
                    ans += 1                
        return ans
                    
        