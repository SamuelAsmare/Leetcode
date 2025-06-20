import numpy as np
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        arr  , Target = np.array(mat) , np.array(target)
        for i in range(1,5):
            if np.array_equal(np.rot90(arr , k=i) , Target):
                return True
        return False
