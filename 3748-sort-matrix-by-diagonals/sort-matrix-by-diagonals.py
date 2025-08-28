class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        diagonal_elements = defaultdict(list)
        for i in range(n):
            for j in range(n):
                diagonal_elements[i - j].append(grid[i][j])
        for d in diagonal_elements:
            if d >= 0:  
                diagonal_elements[d].sort(reverse=True)   
            else:       
                diagonal_elements[d].sort()         

        for i in range(n):
            for j in range(n):
                grid[i][j] = diagonal_elements[i - j].pop(0)

        return grid
