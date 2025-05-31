class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        cols , ans = [list(column) for column in zip(*matrix)] , []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if max(cols[j]) == matrix[i][j] and min(matrix[i]) == matrix[i][j]:
                    ans.append(matrix[i][j])
        return ans


