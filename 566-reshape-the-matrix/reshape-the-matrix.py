import numpy as np
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat)*len(mat[0]) != r*c:
            return mat
        arr = np.array(mat)
        arr = arr.reshape(r,c)
        return arr.tolist()