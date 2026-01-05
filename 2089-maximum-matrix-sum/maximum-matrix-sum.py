class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        totalsum = negativecount = 0
        minabs = float('inf')
        for row in matrix:
            for val in row:
                totalsum += abs(val)
                if val < 0:
                    negativecount += 1
                minabs = min(minabs, abs(val))
                
        if negativecount % 2 == 0:
            return totalsum
        else:
            return totalsum - 2 * minabs