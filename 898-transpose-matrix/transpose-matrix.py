import numpy as np
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        matrix = np.array(matrix)
        tra = matrix.T
        return tra.tolist()