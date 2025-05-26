class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n , result = len(grid) , []
        for i in range(n - 2):
            row = []
            for j in range(n - 2):
                max_val = -1
                for x in range(i, i + 3):
                    for y in range(j, j + 3):
                        max_val = max(max_val, grid[x][y])
                row.append(max_val)
            result.append(row)

        return result
