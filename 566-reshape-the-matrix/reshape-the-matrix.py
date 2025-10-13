import numpy as sam
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat) * len(mat[0]) != r*c:
            return mat
        arr = sam.array(mat)
        ans = arr.reshape(r,c)
        return ans.tolist()
        