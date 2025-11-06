class Solution:
    def helper(self , label , n):
        row = n-1-((label - 1)//n)
        col = (label-1)%n
        if (n-1-row) & 1:
            col = n - 1 - col
        return [row , col]
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        # we need the row column version of the square (helper function)
        # we will use BFS since it is a shortest path
        # hash map for the visited cells
        # what should heper function return
        n = len(board)
        q = deque([(1,0)])
        visited = set([1])
        while q:
            label , distance = q.popleft()
            
            for i in range(1,7):
                next_label = label + i
                row , col = self.helper(next_label,n)
                if board[row][col] != -1:
                    next_label = board[row][col]
                if next_label == n**2:
                    return distance + 1
                if next_label not in visited:
                    q.append((next_label,distance+1))
                    visited.add(next_label)
        return -1
                

