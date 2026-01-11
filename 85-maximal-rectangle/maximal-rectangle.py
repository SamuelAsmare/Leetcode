class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        cols = len(matrix[0])
        heights = [0] * cols
        max_area = 0
        for row in matrix:
            for j in range(cols):
                if row[j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0
            stack = []
            for i in range(cols + 1):
                cur_height = heights[i] if i < cols else 0

                while stack and cur_height < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    width = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, h * width)

                stack.append(i)

        return max_area
