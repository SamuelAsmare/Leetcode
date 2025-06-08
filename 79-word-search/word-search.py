class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        def backtrack(row, col, index):
            if index == len(word):
                return True
            if row < 0 or row >= m or col < 0 or col >= n or board[row][col] != word[index]:
                return False
            temp  , board[row][col] = board[row][col] ,  "sam"
            found = (
                backtrack(row + 1, col, index + 1) or
                backtrack(row - 1, col,  index + 1) or
                backtrack(row, col + 1, index + 1) or
                backtrack(row, col - 1, index + 1))

            board[row][col] = temp
            return found
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and backtrack(i, j, 0):
                    return True
        return False
